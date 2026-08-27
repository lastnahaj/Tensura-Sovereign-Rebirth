package io.github.lastnahaj.tsr.compat.uniquemonsters.mixin;

import dev.architectury.registry.registries.Registrar;
import io.github.lastnahaj.tsr.compat.uniquemonsters.TsrUniqueMonstersCompat;
import net.minecraft.resources.ResourceKey;
import org.spongepowered.asm.mixin.Final;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

@Mixin(
        targets = "dev.architectury.registry.registries.forge.RegistrarManagerImpl$RegistryProviderImpl",
        remap = false
)
abstract class ArchitecturyRegistryProviderMixin {
    @Shadow @Final private String modId;

    @Inject(
            method = "get(Lnet/minecraft/resources/ResourceKey;)Ldev/architectury/registry/registries/Registrar;",
            at = @At("HEAD"),
            cancellable = true,
            require = 1,
            remap = false
    )
    private void tsr$resolveUniqueMonstersSkillRegistrar(
            ResourceKey<?> registryKey,
            CallbackInfoReturnable<Registrar<?>> callbackInfo
    ) {
        Registrar<?> registrar = TsrUniqueMonstersCompat.resolveUniqueMonstersSkillRegistrar(modId, registryKey);
        if (registrar != null) {
            callbackInfo.setReturnValue(registrar);
        }
    }
}
