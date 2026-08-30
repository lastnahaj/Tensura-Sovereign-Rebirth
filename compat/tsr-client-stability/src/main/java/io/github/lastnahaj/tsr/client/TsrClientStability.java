package io.github.lastnahaj.tsr.client;

import net.minecraft.client.Minecraft;
import net.neoforged.api.distmarker.Dist;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.fml.common.Mod;
import net.neoforged.fml.event.lifecycle.FMLLoadCompleteEvent;
import net.neoforged.neoforge.client.event.ClientTickEvent;
import net.neoforged.neoforge.common.NeoForge;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.concurrent.atomic.AtomicBoolean;

@Mod(TsrClientStability.MOD_ID)
public final class TsrClientStability {
    public static final String MOD_ID = "tsr_client_stability";

    private static final Logger LOGGER = LoggerFactory.getLogger("TSR Client Stability");
    private static final AtomicBoolean OPTIONS_RELOADED = new AtomicBoolean();

    public TsrClientStability(IEventBus modEventBus, Dist dist) {
        if (!dist.isClient()) {
            return;
        }

        modEventBus.addListener(TsrClientStability::onLoadComplete);
        NeoForge.EVENT_BUS.addListener(TsrClientStability::onClientTick);
    }

    private static void onLoadComplete(FMLLoadCompleteEvent event) {
        event.enqueueWork(() -> reloadPreservedOptions("mod loading completion"));
    }

    private static void onClientTick(ClientTickEvent.Post event) {
        reloadPreservedOptions("first client tick");
    }

    private static void reloadPreservedOptions(String source) {
        if (OPTIONS_RELOADED.get()) {
            return;
        }

        Minecraft minecraft = Minecraft.getInstance();
        if (minecraft.options == null) {
            return;
        }

        try {
            minecraft.options.load();
            StartupKeybindGuard.release();
            OPTIONS_RELOADED.set(true);
            LOGGER.info("Reloaded preserved client options after {}.", source);
        } catch (RuntimeException exception) {
            LOGGER.error("Unable to reload preserved client options after {}.", source, exception);
        }
    }
}
