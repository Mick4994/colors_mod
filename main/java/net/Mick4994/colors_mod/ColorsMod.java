package net.Mick4994.colors_mod;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.item.v1.FabricItemSettings;
import net.minecraft.block.AbstractBlock;
import net.minecraft.block.Block;
import net.minecraft.block.Material;
import net.minecraft.item.BlockItem;
import net.minecraft.item.Item;
import net.minecraft.item.ItemGroup;
import net.minecraft.util.Identifier;
import net.minecraft.util.registry.Registry;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ColorsMod implements ModInitializer {

	public static final String MOD_ID = "colors_mod";
	public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);
	// new blocks
	// new blockItem

	
	@Override
	public void onInitialize() {


		LOGGER.info("Hello Fabric world!");
	}

}
