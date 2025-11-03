<script>
    let algorithms = ["k-Nearest Neighbors", "k-Means Clustering"];
    let games = ["Nier", "Silent Hill f", "Bloons Tower Defense 6"];
    let inputSizes = [100, 1000, 10000, 100000];

    let algorithmInput = $state();
    let nameInput = $state();

    let suggestedGames = $derived(
        nameInput
            ? games.filter((game) =>
                  game.toLowerCase().includes(nameInput.toLowerCase()),
              )
            : [],
    );
</script>

<div class="container">
    <div class="container-title">
        <p class="title">Recosteam</p>
    </div>
    <div class="container-border"></div>

    <div class="container-inputarea">
        <div class="container-inputarea-algorithm">
            <p>Please Choose the desired algorithm:</p>
            <select bind:value={algorithmInput}>
                {#each algorithms as algo}
                    <option>{algo}</option>
                {/each}
            </select>
        </div>

        <div class="container-inputarea-game">
            <p>Please name your game:</p>
            <input
                type="text"
                bind:value={nameInput}
                placeholder="Choose a game..."
            />
            {#if suggestedGames.length > 0}
                <div class="container-inputarea-game-suggestions">
                    {#each suggestedGames as game}
                        <button
                            type="button"
                            onclick={() => {
                                nameInput = game;
                                suggestedGames = [];
                            }}
                        >
                            {game}
                        </button>
                    {/each}
                </div>
            {/if}
        </div>

        <div class=container-inputarea-game-datasize>
            
        </div>
    </div>
    <div class="container-border"></div>
</div>

<style>
    .container {
        background-color: #2b2b2b;
        display: flex;
        flex-direction: column;
        align-items: center;
        border-radius: 0 1em 1em 0;
        height: 100%;
        width: auto;
        color: #d7dbe0;
        font-family: sans-serif;
        padding: 0.8em;
        margin: 0.6em 0.6em 0.6em 0;
    }
    p {
        margin: 0;
        padding: 0;
    }
    .container-border {
        border: solid #c2c8d1;
        border-width: 0 0 0.002em 0;
        width: 100%;
        padding: 0;
        margin: 0.4em 0 0 0;
    }
    .container-title {
        padding: 0 2em;
        margin: 0;
        font-size: 2em;
        font-weight: bold;
    }

    .container-inputarea {
        display: flex;
        flex-direction: column;
        align-items: left;
        justify-content: center;
        gap: 0.8em;
        width: 100%;
        font-family: sans-serif;
        color: #d7dbe0;
        font-weight: bold;
    }
    .container-inputarea-algorithm {
        width: 100%;
    }
    .container-inputarea-algorithm select {
        height: 2.4em;
        width: 100%;
        text-justify: center;
        box-sizing: border-box;
        border: none;
        background: #1f1e1e;
        color: #d7dbe0;
        font-size: 1em;
        outline: none;
    }

    .container-inputarea-game {
        width: 100%;
    }

    .container-inputarea-game input {
        height: 2.4em;
        width: 100%;
        border: none;
        background: #1f1e1e;
        color: #d7dbe0;
        text-justify: center;
        font-family: sans-serif;
        font-size: 1em;
        box-sizing: border-box;
        outline: none;
    }

    .container-inputarea-game-suggestions {
        position: sticky;
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: 0;
        border: solid #c2c8d1;
        border-width: 0.002em 0 0 0;
        background: #1f1e1e;
        border-radius: 0 0 0.8em 0.8em;
    }
    .container-inputarea-game-suggestions button {
        width: 100%;
        margin: 0;
        border: none;
        font-size: 0.8em;
        color: #d7dbe0;
        background-color: transparent;
        text-align: left;
        padding: 0.4em 0.8em;
    }
</style>
