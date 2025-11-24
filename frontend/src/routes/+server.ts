import { dataBase } from "$lib/server/gameDataBase";
import type { RequestHandler } from "@sveltejs/kit";
import type { SteamGame } from "$lib/types";
import { json } from "@sveltejs/kit";

await dataBase.loadData();
console.log("Server: Loading process done.");


export const GET: RequestHandler = async ({ url }) => {
    if (url.searchParams.get("param") == "names") {
        return json(await dataBase.getGameNames());
    } 
    
    const params = new URLSearchParams({
        gameName: url.searchParams.get("gameName")!,
        algorithm: url.searchParams.get("algorithm")!,
        dataSize: url.searchParams.get("dataSize")!
    });

    let response = await fetch(`http://127.0.0.1:8000/api/?${params}`)
    let gameIds: number[] = await response.json();

    let games: SteamGame[] = [];
    for (let i of gameIds) {
        games.push(await dataBase.getGame(i));
        console.log(i);
    }

    return json(games);
}

