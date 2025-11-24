export interface SteamGame {
    name : string;
    categories: string[];
    short_description: string;
    tags: string[];
    metacritic_score: number;
    positive: number;
    negative: number;
    header_image: string;
}

export interface GameRequest {
    gameName: string;
    algorithm: string;
    dataSize: string;
}