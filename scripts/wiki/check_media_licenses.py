"""Regression checks for file-specific media licensing decisions."""
import unittest
import json
from pathlib import Path

from sync_tensura_wiki import TEXT_LICENSE_URL, determine_license, prepare_media


FOOTER = {"name": "CC BY-SA 4.0", "url": TEXT_LICENSE_URL, "evidence": "Page-content footer"}


class FileLicenseTests(unittest.TestCase):
    def test_reviewed_unconfirmed_images_are_not_distributed(self):
        root = Path(__file__).resolve().parents[2]
        reviews = json.loads((root / 'data/media-file-reviews.json').read_text(encoding='utf-8'))['reviews']
        media = {record['source_file_page']: record for namespace in ('tensura', 'mysticism') for record in json.loads((root / f'data/upstream_{namespace}_media.json').read_text(encoding='utf-8'))['media']}
        for review in reviews:
            with self.subTest(file=review['source_title']):
                record = media[review['file_page']]
                self.assertIsNone(record['license'])
                self.assertEqual(record['import_status'], 'skipped-license')
                self.assertNotIn('local_path', record)
                self.assertFalse((root / 'docs' / record['withdrawn_local_path']).exists())
                self.assertTrue((root / 'docs' / review['replacement_asset']).is_file())

    def test_footer_is_not_an_image_license(self):
        self.assertIsNone(determine_license({"_file_page_checked": True}, FOOTER)[0])

    def test_unchecked_rendered_page_is_rejected(self):
        self.assertIsNone(determine_license({"_wikitext": "{{CC-BY-SA-4.0}}"}, FOOTER)[0])

    def test_explicit_file_license_is_accepted(self):
        record = {"_file_page_checked": True, "_wikitext": "{{CC-BY-SA-4.0}}"}
        self.assertEqual(determine_license(record, FOOTER)[:2], ("CC BY-SA 4.0", TEXT_LICENSE_URL))

    def test_expanded_ownership_notice_takes_precedence(self):
        record = {
            "_file_page_checked": True,
            "_wikitext": "{{CC-BY-SA-4.0}}",
            "_file_page_text": "This file is owned by the applicable game studio and/or its licensors.",
        }
        self.assertIsNone(determine_license(record, FOOTER)[0])

    def test_non_free_template_is_rejected(self):
        record = {"_file_page_checked": True, "_wikitext": "{{Non-free|CC-BY-SA-4.0}}"}
        self.assertIsNone(determine_license(record, FOOTER)[0])

    def test_game_license_template_is_not_creative_commons(self):
        record = {"_file_page_checked": True, "_wikitext": "{{License|game}}"}
        self.assertIsNone(determine_license(record, FOOTER)[0])

    def test_ownership_notice_prevents_download(self):
        class Client:
            refresh = False

            def get_text(self, url, cache):
                return '<div id="mw-content-text"><p>This file is owned by the applicable game studio and/or its licensors.</p></div><footer>Page content is under CC BY-SA 4.0</footer>'

            def download(self, url, destination):
                raise AssertionError("Unconfirmed image must not be downloaded")

        record = {
            "source_title": "Example.png", "source_url": "https://tensura.wiki.gg/images/Example.png",
            "source_file_page": "https://tensura.wiki.gg/wiki/File:Example.png",
        }
        records, _, _ = prepare_media(Client(), [record], [], FOOTER)
        self.assertEqual(records[0]["import_status"], "skipped-license")
        self.assertNotIn("_file_page_text", records[0])


if __name__ == "__main__":
    unittest.main()
