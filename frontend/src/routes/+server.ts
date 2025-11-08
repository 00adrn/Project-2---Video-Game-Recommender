import { dataBase } from "$lib/server/gameDataBase";
import type { RequestHandler } from "@sveltejs/kit";
import type { SteamGame } from "$lib/types";
import { json } from "@sveltejs/kit";

await dataBase.loadData();
console.log("Server: Loading process done.");


export const GET: RequestHandler = async ({ url }) => {
    if (url.searchParams.get("params") == "params") {
        return json(await dataBase.getGameNames());
    }
    let games: SteamGame[] = [];
    for (let i = 0; i < 100; i++)
        games.push(await dataBase.getGame(i));

    return json(games);
}

