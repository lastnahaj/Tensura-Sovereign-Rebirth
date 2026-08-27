package io.github.lastnahaj.tsr.compat.uniquemonsters;

import dev.architectury.registry.registries.Registrar;
import net.crypticmc.tr_unique_monsters.registry.skill.ExtraSkills;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceKey;
import net.minecraft.resources.ResourceLocation;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.fml.common.Mod;
import net.neoforged.fml.event.lifecycle.FMLCommonSetupEvent;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.concurrent.atomic.AtomicBoolean;

@Mod(TsrUniqueMonstersCompat.MOD_ID)
public final class TsrUniqueMonstersCompat {
    public static final String MOD_ID = "tsr_unique_monsters_compat";

    private static final Logger LOGGER = LoggerFactory.getLogger("TSR Unique Monsters Compat");
    private static final ResourceLocation SKILL_REGISTRY_ID =
            ResourceLocation.fromNamespaceAndPath("manascore_skill", "skills");
    private static final ResourceLocation APPRAISAL_EYE_ID =
            ResourceLocation.fromNamespaceAndPath("tr_unique_monsters", "appraisal_eye");
    private static final AtomicBoolean PREMATURE_CALL_INTERCEPTED = new AtomicBoolean();
    private static final AtomicBoolean SAFE_REGISTRATION_INVOKED = new AtomicBoolean();
    private static final AtomicBoolean MOD_CONSTRUCTED = new AtomicBoolean();
    private static volatile Registrar<?> manasCoreSkillRegistrar;
    private static volatile ResourceKey<?> manasCoreSkillRegistryKey;

    public TsrUniqueMonstersCompat(IEventBus modEventBus) {
        if (!MOD_CONSTRUCTED.compareAndSet(false, true)) {
            throw compatibilityFailure("The compatibility mod was constructed more than once.");
        }
        modEventBus.addListener(this::verifyRegisteredSkills);
    }

    public static void interceptPrematureRegistration() {
        if (!PREMATURE_CALL_INTERCEPTED.compareAndSet(false, true)) {
            throw compatibilityFailure("The premature Unique Monsters skill registration path ran more than once.");
        }
        LOGGER.info("Deferred Unique Monsters skill registration until ManasCore skill registry initialization.");
    }

    public static void registerAfterManasCoreSkillRegistryConstruction(
            Registrar<?> registrar,
            ResourceKey<?> registryKey
    ) {
        if (!SAFE_REGISTRATION_INVOKED.compareAndSet(false, true)) {
            throw compatibilityFailure("Unique Monsters skill registration was invoked more than once.");
        }
        if (!SKILL_REGISTRY_ID.equals(registryKey.location())) {
            throw compatibilityFailure("ManasCore constructed an unexpected skill registry key: " + registryKey);
        }
        manasCoreSkillRegistrar = registrar;
        manasCoreSkillRegistryKey = registryKey;
        try {
            ExtraSkills.init();
        } catch (RuntimeException exception) {
            throw compatibilityFailure(
                    "Unable to register Unique Monsters skills after SkillRegistry construction.",
                    exception
            );
        }
        LOGGER.info("Unique Monsters skill registration submitted after ManasCore SkillRegistry construction.");
    }

    public static Registrar<?> resolveUniqueMonstersSkillRegistrar(String modId, ResourceKey<?> registryKey) {
        if (!"tr_unique_monsters".equals(modId) || !registryKey.equals(manasCoreSkillRegistryKey)) {
            return null;
        }
        return manasCoreSkillRegistrar;
    }

    private void verifyRegisteredSkills(FMLCommonSetupEvent event) {
        if (!PREMATURE_CALL_INTERCEPTED.get()) {
            throw compatibilityFailure(
                    "The expected Unique Monsters registration call was not intercepted; upstream structure changed."
            );
        }
        if (!SAFE_REGISTRATION_INVOKED.get()) {
            throw compatibilityFailure(
                    "The ManasCore SkillRegistry class-initialization hook did not run; upstream structure changed."
            );
        }
        Registry<?> skillRegistry = (Registry<?>) BuiltInRegistries.REGISTRY.get(SKILL_REGISTRY_ID);
        if (skillRegistry == null) {
            throw compatibilityFailure("Expected registry manascore_skill:skills is unavailable during common setup.");
        }
        if (!skillRegistry.containsKey(APPRAISAL_EYE_ID)) {
            throw compatibilityFailure(
                    "Expected Unique Monsters skill tr_unique_monsters:appraisal_eye was not registered."
            );
        }
        LOGGER.info("Unique Monsters skills registered successfully: {}.", APPRAISAL_EYE_ID);
    }

    private static IllegalStateException compatibilityFailure(String message) {
        return new IllegalStateException("TSR Unique Monsters Compat: " + message);
    }

    private static IllegalStateException compatibilityFailure(String message, Throwable cause) {
        return new IllegalStateException("TSR Unique Monsters Compat: " + message, cause);
    }
}
