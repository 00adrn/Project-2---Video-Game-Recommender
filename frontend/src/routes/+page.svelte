<script lang="ts">
    import GameCard from "$lib/components/GameCard.svelte";
    import Sidebar from "$lib/components/Sidebar.svelte";
    import Header from "$lib/components/Header.svelte";
    import type {SteamGame} from '$lib/types.ts';

    let testGame: SteamGame = {
        imageUrl: "https://cdn.akamai.steamstatic.com/steam/apps/524220/header.jpg?t=1646911723",
        title: "testgame",
        genre: "testgenre",
        description: "testdescription",
        rating: "testrating",
        price: "testprice",
    };
    let steamColors = [
        "#171a21",
        "#1b2838",
        "#2a475e",
        "#66c0f4",
        "#c7d5e0"];

    let games: SteamGame[] = $state([testGame, testGame, testGame, testGame, testGame, testGame, testGame, testGame, testGame, testGame, testGame, testGame, testGame]);
    let algorithmInput : string | undefined = $state() ;
    let nameInput : string | undefined = $state() ;
    let dataSizeInput : string | undefined = $state() ;
</script>

<div class="container" style="--deg: 90deg; --gradient-1:#FFFFFFFF; --gradient-2:{steamColors[4]};">
    <div class="container-sidebar">
        <Sidebar bind:algorithmInput={algorithmInput} bind:nameInput={nameInput} bind:dataSizeInput= {dataSizeInput} colors={steamColors} />
    </div>
    <div class="container-games">
        <div class="container-games-header">
            <Header algorithmName={algorithmInput} colors={steamColors} />
        </div>
        <div class="container-games-list">
            {#if games.length == 0}
            <div class="container-games-list-empty">
                <p>Games will appear here!</p>
            </div>
            {:else}
                {#each games as game}
                    <GameCard game={game} />
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
        background: linear-gradient(var(--deg), var(--gradient-1), var(--gradient-2));
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