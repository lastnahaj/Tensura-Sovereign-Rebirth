package io.github.lastnahaj.tsr.compat.uniquemonsters.mixin;

import dev.architectury.registry.registries.Registrar;
import io.github.lastnahaj.tsr.compat.uniquemonsters.TsrUniqueMonstersCompat;
import net.minecraft.resources.ResourceKey;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Final;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

@Mixin(targets = "io.github.manasmods.manascore.skill.impl.SkillRegistry", remap = false)
abstract class ManasCoreSkillRegistryMixin {
    @Shadow @Final public static Registrar<?> SKILLS;
    @Shadow @Final public static ResourceKey<?> KEY;

    @Inject(method = "<clinit>", at = @At("TAIL"), require = 1, remap = false)
    private static void tsr$registerUniqueMonstersSkills(CallbackInfo callbackInfo) {
        TsrUniqueMonstersCompat.registerAfterManasCoreSkillRegistryConstruction(SKILLS, KEY);
    }
}
