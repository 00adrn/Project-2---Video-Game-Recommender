<script lang="ts">
    let {
        imageUrl = "https://cdn.akamai.steamstatic.com/steam/apps/524220/header.jpg?t=1646911723",
        title = "Steam Game Title",
        genre = "Steam Game Genres",
        rating = "Rating / Score given to the game (i.e. metacritic score)",
        description = "Description of the game provided by Steam.",
        price = "99.99",
    } = $props();
</script>

<div class="card">
    <div class="card-content">
        <div class="card-content-title">
            <p>{title}</p> 
        </div>
        <div class="card-content-genre">
            <p>{genre}</p>
        </div>

        <div class="card-content-description">
            <p>{description}</p>
        </div>

        <div class="card-content-rating">
            <p>{rating}</p>
        </div>

    </div>

    <div class="card-price">
        <p>${price}</p>
    </div>
</div>

<style>
    .card {
        background-color: #4d4d4d;
        display: flex;
        flex-direction: row;
        border-radius: 1em;
        align-items: center;
        justify-content: space-between;
        color: #d7dbe0;
        font-family: sans-serif;
        margin: .5em;
        width: auto;
        border: solid #c2c8d1;
        border-width: .1em 0;
    }
    

    .card-content {
        width: 100%;
        height: auto;
        display: flex;
        flex-direction: column;
        padding: .8rem;
        gap: .2em;

    }

    .card-content-title {
        font-size: 1.2em;
    }
    .card-content-genre {
        color: #c2c8d1;
        font-size: .6em;
        padding: .2em 0 0 0;
    }
    .card-content-description {
        color: #c2c8d1;
        font-size: .6em;
        padding: .2em 0 0 0;
    }

    .card-content-rating {
        color: #c2c8d1;
        font-size: .6em;
        padding: .2em 0 0 0;
    }

    .card-price {
        display: flex;
        align-items: right;
        padding: 0 .5rem 0 .25rem;
    }

    p {
        padding: 0;
        margin: 0;
    }
</style>    
