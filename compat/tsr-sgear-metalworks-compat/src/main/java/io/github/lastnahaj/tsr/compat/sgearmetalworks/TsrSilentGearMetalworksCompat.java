package io.github.lastnahaj.tsr.compat.sgearmetalworks;

import com.mojang.logging.LogUtils;
import cy.jdkdigital.productivemetalworks.common.datamap.UnitMap;
import cy.jdkdigital.productivemetalworks.registry.MetalworksRegistrator;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.packs.PackType;
import net.minecraft.server.packs.repository.Pack;
import net.minecraft.server.packs.repository.PackSource;
import net.minecraft.world.level.material.Fluid;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.fml.ModList;
import net.neoforged.fml.common.Mod;
import net.neoforged.neoforge.common.NeoForge;
import net.neoforged.neoforge.event.AddPackFindersEvent;
import net.neoforged.neoforge.registries.BaseMappedRegistry;
import net.neoforged.neoforge.registries.datamaps.DataMapsUpdatedEvent;
import org.slf4j.Logger;

import java.util.List;
import java.util.Map;
import java.util.Set;

@Mod(TsrSilentGearMetalworksCompat.MOD_ID)
public final class TsrSilentGearMetalworksCompat {
    public static final String MOD_ID = "tsr_sgear_metalworks_compat";
    private static final Logger LOGGER = LogUtils.getLogger();
    private static final List<ResourceLocation> REQUIRED_FLUIDS = List.of(
            id("productivemetalworks:molten_iron"),
            id("sgearmetalworks:molten_azure_electrum"),
            id("sgearmetalworks:molten_azure_silver"),
            id("sgearmetalworks:molten_blaze_gold"),
            id("sgearmetalworks:molten_crimson_iron"),
            id("sgearmetalworks:molten_crimson_steel"),
            id("sgearmetalworks:molten_tyrian_steel"),
            id("sgearmetalworks:molten_uru_metal")
    );
    private static final List<ResourceLocation> SILENT_GEMS_FLUIDS = List.of(
            id("sgearmetalworks:molten_alexandrite"),
            id("sgearmetalworks:molten_ammolite"),
            id("sgearmetalworks:molten_aquamarine"),
            id("sgearmetalworks:molten_black_diamond"),
            id("sgearmetalworks:molten_carnelian"),
            id("sgearmetalworks:molten_citrine"),
            id("sgearmetalworks:molten_garnet"),
            id("sgearmetalworks:molten_heliodor"),
            id("sgearmetalworks:molten_iolite"),
            id("sgearmetalworks:molten_kyanite"),
            id("sgearmetalworks:molten_moldavite"),
            id("sgearmetalworks:molten_opal"),
            id("sgearmetalworks:molten_pearl"),
            id("sgearmetalworks:molten_peridot"),
            id("sgearmetalworks:molten_rose_quartz"),
            id("sgearmetalworks:molten_ruby"),
            id("sgearmetalworks:molten_sapphire"),
            id("sgearmetalworks:molten_tanzanite"),
            id("sgearmetalworks:molten_topaz"),
            id("sgearmetalworks:molten_turquoise"),
            id("sgearmetalworks:molten_white_diamond")
    );

    public TsrSilentGearMetalworksCompat(IEventBus modBus) {
        modBus.addListener(this::addPackFinders);
        NeoForge.EVENT_BUS.addListener(this::verifyFluidUnitMap);
    }

    private void addPackFinders(AddPackFindersEvent event) {
        if (event.getPackType() != PackType.SERVER_DATA) {
            return;
        }

        event.addPackFinders(
                ResourceLocation.fromNamespaceAndPath(MOD_ID, "datapack"),
                PackType.SERVER_DATA,
                Component.literal("TSR Silent Gear Metalworks Compat"),
                PackSource.BUILT_IN,
                true,
                Pack.Position.TOP
        );
    }

    @SuppressWarnings("unchecked")
    private void verifyFluidUnitMap(DataMapsUpdatedEvent event) {
        if (event.getRegistryKey() != Registries.FLUID) {
            return;
        }

        Registry<Fluid> registry = (Registry<Fluid>) event.getRegistry();
        if (!(registry instanceof BaseMappedRegistry<?>)) {
            throw new IllegalStateException("NeoForge fluid registry does not expose data maps");
        }

        BaseMappedRegistry<Fluid> mappedRegistry = (BaseMappedRegistry<Fluid>) registry;
        Map<?, UnitMap> unitMap = mappedRegistry.getDataMap(MetalworksRegistrator.UNIT_MAP);
        Set<ResourceLocation> mappedFluids = unitMap.keySet().stream()
                .map(key -> ((net.minecraft.resources.ResourceKey<?>) key).location())
                .collect(java.util.stream.Collectors.toUnmodifiableSet());

        List<ResourceLocation> missingRequired = REQUIRED_FLUIDS.stream()
                .filter(fluid -> !mappedFluids.contains(fluid))
                .toList();
        if (!missingRequired.isEmpty()) {
            throw new IllegalStateException("Required Metalworks unit mappings are missing: " + missingRequired);
        }

        if (!ModList.get().isLoaded("silentgems")) {
            List<ResourceLocation> unexpectedOptional = SILENT_GEMS_FLUIDS.stream()
                    .filter(mappedFluids::contains)
                    .toList();
            if (!unexpectedOptional.isEmpty()) {
                throw new IllegalStateException("Silent Gems unit mappings loaded without Silent Gems: " + unexpectedOptional);
            }
        }

        LOGGER.info(
                "Verified Metalworks fluid unit map: {} installed mappings present, {} unavailable Silent Gems mappings excluded.",
                REQUIRED_FLUIDS.size(),
                ModList.get().isLoaded("silentgems") ? 0 : SILENT_GEMS_FLUIDS.size()
        );
    }

    private static ResourceLocation id(String value) {
        return ResourceLocation.parse(value);
    }
}
