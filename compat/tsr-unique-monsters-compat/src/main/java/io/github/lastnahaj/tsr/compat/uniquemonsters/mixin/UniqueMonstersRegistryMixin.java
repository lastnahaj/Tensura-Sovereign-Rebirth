package io.github.lastnahaj.tsr.compat.uniquemonsters.mixin;

import io.github.lastnahaj.tsr.compat.uniquemonsters.TsrUniqueMonstersCompat;
import net.crypticmc.tr_unique_monsters.registry.TRUniqueMobsRegistry;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Redirect;

@Mixin(value = TRUniqueMobsRegistry.class, remap = false)
abstract class UniqueMonstersRegistryMixin {
    @Redirect(
            method = "injectInit()V",
            at = @At(
                    value = "INVOKE",
                    target = "Lnet/crypticmc/tr_unique_monsters/registry/skill/ExtraSkills;init()V",
                    remap = false
            ),
            require = 1,
            remap = false
    )
    private static void tsr$deferExtraSkillsRegistration() {
        TsrUniqueMonstersCompat.interceptPrematureRegistration();
    }
}
