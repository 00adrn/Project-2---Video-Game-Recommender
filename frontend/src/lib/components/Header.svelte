<script lang="ts">
    let { algorithmName = "algorithmName", colors = [] } = $props();
</script>

<div class="container" style="--deg: 270deg; --gradient-1:{colors[1]}; --gradient-2:{colors[2]};">
    <p>Recommendations based on {algorithmName}</p>
</div>

<style>
    .container {
        background: linear-gradient(var(--deg), var(--gradient-1), var(--gradient-2));
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: auto;
        width: auto;
        color: #c7d5e0;
        font-family: sans-serif;
        font-size: 2em;
        font-weight: bold;
        border:solid #1b2838;
        border-width: 0 0 .1em 0;
    }
    p {
        margin: 0;
        padding: .4em;
    }
</style>