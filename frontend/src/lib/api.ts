 import type { SteamGame, GameRequest } from "./types.ts"

async function getRecommendations(game : GameRequest): Promise<SteamGame[]> {
    const params = new URLSearchParams({
        gameName: game.gameName,
        algorithm: game.algorithm,
        dataSize: game.dataSize
    });

    console.log(`Sending request to: http://localhost:5173/?${params}`);
    const response = await fetch(`http://localhost:5173/?${params}`);

    if (!response.ok)
        throw new Error("Error sending request");

    const data = await response.json();
    let games: SteamGame[] = []; 
    games = data as SteamGame[];

    return games;
}

async function getGameNames() : Promise<string[]> {
    const response = await fetch("http://localhost:5173?param=names");
    const data = await response.json();
    let names: string[] = data as string[];
    return names;

}

export const api = {getRecommendations, getGameNames};