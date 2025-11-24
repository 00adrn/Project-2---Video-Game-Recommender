<script lang="ts">
    let algorithms = ["k-Nearest Neighbors", "Heuristic Based Algorithm"];
    let inputSizes = [100000, 10000, 1000, 100, 10];

    let {
        algorithmInput = $bindable(),
        nameInput = $bindable(),
        dataSizeInput = $bindable(),
        colors = [],
        gameNames = [],
        buttonFunction,
    } = $props();

    let filteredGameNames = $derived( nameInput.length > 0 ? gameNames.filter((name) => name.toLowerCase().includes(nameInput.toLowerCase())).slice(0, 10) : [],);

    const setName = (index:number) => {
        nameInput = filteredGameNames[index];
        filteredGameNames = [];
    }
</script>

<div
    class="container"
    style="--deg: 20deg; --gradient-1:{colors[0]}; --gradient-2:{colors[2]};"
>
    <img src="/RecoSteam.png" alt="RecoSteam Logo" class="my-image"/>
    <div class="container-border"></div>

    <div
        class="container-inputarea"
        style="background: #171a21; padding: .4em; border-radius: 0.4em;"
    >
        <div class="container-inputarea-algorithm">
            <p>Choose Sorting Algorithm:</p>
            <select bind:value={algorithmInput} >
                {#each algorithms as algo, i}
                    <option value = {algo} selected>{algo}</option>
                {/each}
            </select>
        </div>

        <div class="container-inputarea-game">
            <p>Please name your game:</p>
            <input
                type="text"
                bind:value={nameInput}
                placeholder="Choose a game..."/>
            {#if nameInput.length > 0}
                <div class="container-inputarea-game-suggestions">
                {#each filteredGameNames as game, i}
                    <button onclick={() => setName(i)}>{game}</button>
                {/each}
                </div>
            {/if}
        </div>

        <div class="container-inputarea-datasize">
            <p>Number of games to pick from:</p>
            <select bind:value={dataSizeInput}>
                {#each inputSizes as size}
                        <option value={size} selected>{size}</option>
                {/each}
            </select>
        </div>
    </div>
    <div class="container-border"></div>
    <div class="container-calculate">
        <button onclick={buttonFunction}>Calculate</button>
    </div>
</div>

<style>
    .container {
        background: linear-gradient(
            var(--deg),
            var(--gradient-1),
            var(--gradient-2)
        );
        display: flex;
        flex-direction: column;
        align-items: center;
        height: 100%;
        min-width: auto;
        color: #d7dbe0;
        font-family: sans-serif;
        padding: 0.8em;
        margin: 0;
        border-width: 0 0.002em 0 0;
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
        margin: 0 0 0;
    }

    .container-inputarea {
        margin-top: 0.5em;
        width: 100%;
        text-align: center;
        font-size: 1.8em;
        display: flex;
        flex-direction: column;
        gap: 1.4em;
        width: 100%;
        font-family: sans-serif;
        font-weight: bold;
    }
    .container-inputarea-algorithm select {
        height: 2.4em;
        width: 100%;
        text-justify: center;
        box-sizing: border-box;
        border: 0.02em solid #171a21;
        border-radius: 0.4em;
        background: #c7d5e0;
        color: #171a21;
        font-size: 1em;
        outline: none;
    }
    .container-inputarea-algorithm select:hover {
        background: white;
    }
    .container-inputarea-game input {
        height: 2.4em;
        width: 100%;
        border: 0.02em solid #171a21;
        border-radius: 0.4em;
        background: #c7d5e0;
        color: #171a21;
        text-justify: center;
        font-family: sans-serif;
        font-size: 1em;
        box-sizing: border-box;
        outline: none;
    }
    .container-inputarea-game input:hover {
        background: white;
    }
    .container-inputarea-game-suggestions {
        display: flex;
        background: #c7d5e0;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border: 0.02em solid #171a21;
        border-radius: 0.4em;
        width:100%;
    }
    .container-inputarea-game-suggestions button {
        border: none;
        background: none; 
        width:100%;
        font-family: sans-serif;
        color: #171a21;
        text-justify: center;
        font-family: sans-serif;
        height:1.2em;
        font-size: .8em;
        overflow:hidden;
    }
    .container-inputarea-datasize select {
        height: 2.4em;
        width: 100%;
        text-justify: center;
        box-sizing: border-box;
        border: 0.02em solid #171a21;
        border-radius: 0.4em;
        background: #c7d5e0;
        color: #171a21;
        font-size: 1em;
        outline: none;
    }
    .container-inputarea-datasize select:hover {
        background: white;
    }
    .container-calculate {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
    }
    .container-calculate button {
        border-radius: 0.4em;
        border: 0.1em solid #c7d5e0;
        background: #1b2838;
        color: #c7d5e0;
        font-family: sans-serif;
        font-weight: bold;
        height: 2.2em;
        font-size: 1.6em;
        width: 100%;
        margin: 1.2em;
    }
    .container-calculate button:hover {
        background: #305d81;
    }
    .my-image {
        width: 225px;
        height: 225px;
    }
</style>
