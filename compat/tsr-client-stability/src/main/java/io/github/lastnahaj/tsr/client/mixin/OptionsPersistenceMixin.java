package io.github.lastnahaj.tsr.client.mixin;

import io.github.lastnahaj.tsr.client.StartupKeybindGuard;
import net.minecraft.client.Options;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

import java.io.File;

@Mixin(Options.class)
abstract class OptionsPersistenceMixin {
    @Shadow
    private File optionsFile;

    @Inject(method = "load", at = @At("HEAD"))
    private void tsr$captureOptionsBeforeLoad(CallbackInfo callbackInfo) {
        StartupKeybindGuard.capture(optionsFile);
    }

    @Inject(method = "save", at = @At("TAIL"))
    private void tsr$restoreUnknownOptionsAfterSave(CallbackInfo callbackInfo) {
        StartupKeybindGuard.restore(optionsFile);
    }
}
