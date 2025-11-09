export interface SteamGame {
    name : string;
    categories: string[];
    short_description: string;
    tags: string[];
    metacritic_score: number;
    positive: number;
    negative: number;
    header: string;
}

export interface GameRequest {
    gameName: string;
    algorithm: string;
    inData: string;
    dataSize: string;
}