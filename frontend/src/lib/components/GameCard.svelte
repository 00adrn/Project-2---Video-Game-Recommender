<script lang="ts">
    import type { SteamGame } from "$lib/types.ts";
    let { game }: { game: SteamGame } = $props();
</script>

<div class="card">
    <div class="card-image">
        <img src={game.imageUrl} alt={game.title} />
    </div>

    <div class="card-content">
        <div class="card-content-title">
            <p>{game.title}</p>
        </div>
        <div class="card-content-genre">
            <p>{game.genre}</p>
        </div>

        <div class="card-content-description">
            <p>{game.description}aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa</p>
        </div>
    </div>
    <div class="card-ratings">
        <p>{game.rating}</p>
    </div>
    <div class="card-price">
        <p>${game.price}</p>
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
        font-size: 1.8em;
    }
    .card-content-genre {
        color: #c7d5e0;
        font-size: 1.6em;
        padding: 0.2em 0 0 0;
    }
    .card-content-description {
        color: #c7d5e0;
        font-size: 1.6em;
        padding: 0.2em 0 0 0;
    }

    .card-content-description p {
        overflow-wrap: break-word;
    }


    .card-price {
        display: flex;
        align-items: right;
        font-size: 1.6em;
        padding: 0 0.5rem 0 0.25rem;
    }
    .card-ratings {
        display: flex;
        align-items: right;
        font-size: 1.6em;
        padding: 0 1rem 0 0.5rem;
    }

    p {
        padding: 0;
        margin: 0;
    }
</style>
