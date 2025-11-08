<script lang="ts">
    let { algorithmName = "algorithmName", colors = [] } = $props();
</script>

<div class="container" style="--deg: -20deg; --gradient-1:{colors[0]}; --gradient-2:{colors[2]};">
    <p>Recommendations based on {algorithmName}</p>
    <div class="container-border"></div>
    
</div>

<style>
    .container {
        background: linear-gradient(var(--deg), var(--gradient-1), var(--gradient-2));
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100%;
        width: auto;
        color: #c7d5e0;
        font-family: sans-serif;
        font-size: 3em;
        font-weight: bold;
        border-width: 0 0 .1em 0;
        padding: 0.1em 2em;
        margin: 0;
        position: relative;
    }
    p {
        margin: 0;
        padding: .4em;
    }
    .container-border {
        border: solid #c7d5e0;
        border-width: 0 0 0.002em 0;
        width: 100%;
        padding: 0;
        margin: 0.175em 0 0 0;
    }
</style>