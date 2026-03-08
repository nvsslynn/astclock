async function updatec(){
    const response = await fetch("/raw")
    const data = await response.json()

    const horas = document.querySelector("#houras")
    const mins = document.querySelector("#minutos")
    const secs = document.querySelector("#secs")

    horas.textContent = data.hour
    mins.textContent = data.mins
    secs.textContent = data.secs
}

setInterval(updatec, 2000)