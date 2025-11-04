<script lang="ts">
    let { algorithmName = "algorithmName" } = $props();
</script>

<div class="container">
    <p>Recommendations based on {algorithmName}</p>
</div>

<style>
    .container {
        background-color: #2b2b2b;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: auto;
        width: auto;
        color: #d7dbe0;
        font-family: sans-serif;
        font-size: 1.2em;
        font-weight: bold;
    }
    p {
        margin: 0;
        padding: .4em;
    }
</style>