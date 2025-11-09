 import type { SteamGame, GameRequest } from "./types.ts"

async function getRecommendations(game : GameRequest): Promise<SteamGame[]> {
    // const params = new URLSearchParams({
    //     gameName: game.gameName,
    //     algorithm: game.algorithm,
    //     inData: game.inData
    // });

    const response = await fetch("http://localhost:5173/?param=reccomendations", {
        method: "GET",
        headers: {
            accept: "application/json"
        }
    })

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