<script lang="ts">
    import type { SteamGame } from "$lib/types.ts";
    let { game }: { game: SteamGame } = $props();

    function getMetacriticScore ()  {return game.metacritic_score != 0 ? game.metacritic_score : "-"}
</script>

<div class="card">
    <div class="card-image">
        <img src={game.header_image} alt={game.name} />
    </div>

    <div class="card-content">
        <div class="card-content-title">
            <p>{game.name}</p>
        </div>
        <div class="card-content-genre">
            <div class="card-content-genre-tags">
                {#each game.tags as tag, i}
                    <p>{tag}</p>
                {/each}
            </div>
        </div>

        <div class="card-content-description">
            <p>{game.short_description}</p>
        </div>
    </div>
    <div class="card-ratings">
        <p>{getMetacriticScore()}</p>
    </div>
</div>

<style>
    .card {
        background-color: #2a475e;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        color: #d7dbe0;
        font-family: sans-serif;
        margin: 0.4em 0.4em 0 .4em;
        width: auto;
        border-radius: 0.4em;
    }
    .card-image {
        width: 12em;
        height: 80%;
        flex-shrink: 0;
        overflow: hidden;
        border-radius: 0.2em;
        margin-left: 0.8em;
    }
    .card-image img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }
    .card-content {
        flex-grow: 1;
        min-width: 0;
        height: auto;
        display: flex;
        flex-direction: column;
        padding: 0.8rem;
        gap: 0.2em;
    }

    .card-content-title {
        font-size: 1.4em;
    }
    .card-content-genre {
        color: #c7d5e0;
        font-size: .4em;
        padding: 0.2em 0 0 0;
    }
    .card-content-genre-tags {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        gap: .8em;

    }
    .card-content-description {
        color: #c7d5e0;
        font-size: .8em;
        padding: 0.2em 0 0 0;
    }

    .card-content-description p {
        overflow-wrap: break-word;
    }
    .card-ratings {
        display: flex;
        align-items: right;
        font-size: .8em;
        padding: 0 1rem 0 0.5rem;
    }
    p {
        padding: 0;
        margin: 0;
    }
</style>
