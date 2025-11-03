<script lang="ts">
    import GameCard from "$lib/components/GameCard.svelte";
    import Sidebar from "$lib/components/Sidebar.svelte";
    import Header from "$lib/components/Header.svelte";
</script>

<div class="container">
    <div class="container-sidebar">
        <Sidebar />
    </div>
    <div class="container-games">
        <div class="container-games-header">
            <Header />
        </div>
        <div class="container-games-list"></div>
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
        background: #1f1e1e;
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
        background: #1f1e1e;
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
