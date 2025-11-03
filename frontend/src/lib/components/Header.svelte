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
        border-radius: 0 0 .6em .6em;
        color: #d7dbe0;
        font-family: sans-serif;
        font-size: 1.2em;
        font-weight: bold;

    }
    p {
        margin: 0;
        padding: 0;
    
    }
</style>