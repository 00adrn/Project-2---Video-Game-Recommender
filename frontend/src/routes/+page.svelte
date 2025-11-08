<script lang="ts">
    import GameCard from "$lib/components/GameCard.svelte";
    import Sidebar from "$lib/components/Sidebar.svelte";
    import Header from "$lib/components/Header.svelte";
    import type { SteamGame, GameRequest } from "$lib/types.ts";
    import { api } from "$lib/api";
    import { onMount } from "svelte";

    let steamColors = ["#171a21", "#1b2838", "#2a475e", "#66c0f4", "#c7d5e0"];

    let gameNames: string[] = $state([]);
    let games: SteamGame[] = $state([]);
    let algorithmInput: string = $state("k-Nearest Neighbors");
    let nameInput: string = $state("");
    let dataSizeInput: string = $state("1000000");

    async function sendRequest() {
        if (nameInput === "" || dataSizeInput === "") return;
        let request: GameRequest = {
            gameName: nameInput,
            algorithm: algorithmInput,
            dataSize: dataSizeInput,
            inData: "1",
        };
        games = await api.getRecommendations(request);
    }

    onMount(async () => {
        gameNames = await api.getGameNames();
    });
</script>

<div
    class="container"
    style="--deg: 90deg; --gradient-1:#FFFFFFFF; --gradient-2:{steamColors[4]};"
>
    <div class="container-sidebar">
        <Sidebar
            bind:algorithmInput
            bind:nameInput
            bind:dataSizeInput
            colors={steamColors}
            {gameNames}
            buttonFunction={sendRequest}
        />
    </div>
    <div class="container-games">
        <div class="container-games-header">
            <Header algorithmName={algorithmInput} colors={steamColors} />
        </div>
        <div class="container-games-list">
            {#if games.length === 0}
                <div class="container-games-list-empty">
                    <p>Games will appear here!</p>
                </div>
            {:else}
                {#each games as game}
                    <GameCard {game} />
                {/each}
            {/if}
        </div>
    </div>
</div>

<style>
    :global(html, body) {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        overflow: hidden;
    }
    .container {
        display: flex;
        flex-direction: row;
        align-items: center;
        height: 100vh;
        padding: 0;
        margin: 0;
        background: linear-gradient(
            var(--deg),
            var(--gradient-1),
            var(--gradient-2)
        );
        gap: 0;
    }
    .container-sidebar {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100%;
    }
    .container-games {
        display: flex;
        flex-direction: column;
        width: 100%;
        height: 100%;
    }
    .container-games-list {
        position: relative;
        display: flex;
        flex-direction: column;
        height: 100vh;
        overflow-y: scroll;
        scrollbar-width: none;
        -ms-overflow-style: none;
    }
    .container-games-list-empty {
        font-family: sans-serif;
        color: black;
        font-size: 6em;
        font-weight: bold;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .container-games-header {
        position: sticky;
        z-index: 1;
        top: 0;
        width: 100%;
        background: transparent;
    }
    .container-games-list::-webkit-scrollbar {
        display: none;
    }
</style>
