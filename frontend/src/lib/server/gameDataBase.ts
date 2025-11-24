import path from "path";
import fs from "fs/promises"
import type { SteamGame } from "$lib/types";

let loaded = false;


async function loadData() {
    if (loaded) return;
    const jsonPath = path.resolve("src/lib/server/data.json");
    const fileContent = await fs.readFile(jsonPath, "utf-8");

    try {
        const keyMatches = fileContent.matchAll(/"(\d+)":\s*\{/g);
        const unorderedKeys = Array.from(keyMatches, match => match[1]);

        const data: Record<string, SteamGame> = JSON.parse(fileContent);
        unorderedKeys.forEach((key, index) => {
            gameData.set(index, data[key]);
        });

        console.log("Data loaded successfully.")
        console.log("First read game: " + gameData.get(0)!.name)
        loaded = true;

    } catch (error) {
        console.log("Error loading data:", error);
    }
}

async function getGame(id: number): Promise<SteamGame> {
    return gameData.get(id)!;
}

async function getGameNames() {
    let names: string[] = [];
    gameData.forEach((game) => {
        names.push(game.name);
    });
    return names;
}

const gameData: Map<number, SteamGame> = new Map<number, SteamGame>();

export const dataBase = {
    loadData,
    getGame,
    getGameNames
}
