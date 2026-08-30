package io.github.lastnahaj.tsr.client;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public final class StartupKeybindGuard {
    private static final Logger LOGGER = LoggerFactory.getLogger("TSR Client Stability");
    private static final Map<String, String> INITIAL_KEYBINDS = new LinkedHashMap<>();

    private static boolean captured;
    private static boolean released;

    private StartupKeybindGuard() {
    }

    public static synchronized void capture(File optionsFile) {
        if (captured || optionsFile == null || !optionsFile.isFile()) {
            return;
        }

        try {
            for (String line : Files.readAllLines(optionsFile.toPath(), StandardCharsets.UTF_8)) {
                int delimiter = line.indexOf(':');
                if (delimiter > 0) {
                    String key = line.substring(0, delimiter);
                    if (key.startsWith("key_")) {
                        INITIAL_KEYBINDS.put(key, line.substring(delimiter + 1));
                    }
                }
            }
            captured = true;
            LOGGER.info("Protected {} keybindings during client startup.", INITIAL_KEYBINDS.size());
        } catch (IOException exception) {
            LOGGER.warn("Unable to protect keybindings before loading options.txt.", exception);
        }
    }

    public static synchronized void restore(File optionsFile) {
        if (!captured || released || optionsFile == null || !optionsFile.isFile()) {
            return;
        }

        try {
            List<String> current = Files.readAllLines(optionsFile.toPath(), StandardCharsets.UTF_8);
            List<String> restored = new ArrayList<>(current.size() + INITIAL_KEYBINDS.size());
            Set<String> found = new LinkedHashSet<>();
            int changed = 0;

            for (String line : current) {
                int delimiter = line.indexOf(':');
                if (delimiter <= 0) {
                    restored.add(line);
                    continue;
                }

                String key = line.substring(0, delimiter);
                String preserved = INITIAL_KEYBINDS.get(key);
                if (preserved == null) {
                    restored.add(line);
                    continue;
                }

                found.add(key);
                String replacement = key + ":" + preserved;
                restored.add(replacement);
                if (!replacement.equals(line)) {
                    changed++;
                }
            }

            for (Map.Entry<String, String> entry : INITIAL_KEYBINDS.entrySet()) {
                if (found.add(entry.getKey())) {
                    restored.add(entry.getKey() + ":" + entry.getValue());
                    changed++;
                }
            }

            if (changed > 0) {
                Files.write(
                        optionsFile.toPath(),
                        restored,
                        StandardCharsets.UTF_8,
                        StandardOpenOption.TRUNCATE_EXISTING
                );
                LOGGER.info("Restored {} keybindings changed by an early client save.", changed);
            }
        } catch (IOException exception) {
            LOGGER.warn("Unable to restore keybindings changed by an early client save.", exception);
        }
    }

    public static synchronized void release() {
        released = true;
        INITIAL_KEYBINDS.clear();
    }
}
