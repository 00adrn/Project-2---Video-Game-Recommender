<script lang="ts">
    let { title="title", rank="1", genre="genre", rating="x/1", description="gamedescription", price="99.99" } = $props();
</script>

<div class="card">
    <div class="card-rank">
        <p> {rank}</p>
    </div>

    <div class="card-content">
        <div class="card-content-title">
            <p> {title}</p>
        </div>

        <div class="card-content-genre">
            <p> {genre}</p>
        </div>

        <div class="card-content-rating">
            <p> {rating}</p>
        </div>

        <div class="card-content-description">
            <p> {description}</p>
        </div>

    </div>

    <div class="card-price">
        <p> ${price}</p>
    </div>
</div>
