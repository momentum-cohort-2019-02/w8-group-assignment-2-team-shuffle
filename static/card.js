document.addEventListener('DOMContentLoaded', function (){
    const viewPreviousButton = document.getElementById('view-previous')
    const viewNextButton = document.getElementById('view-next')
    const cardCount = document.getElementById('card-count')
    
    cardArray = createArray(cardCount.innerText)
    shuffledCardArray = shuffle(cardArray)
    // console.log(shuffledCardArray)
    window.cardArray = shuffledCardArray
    window.currentCardIndex = 0
    showCard(0)

    viewPreviousButton.addEventListener('click', event => {
        //when button gets clicked, call viewPreviousCard function
        viewPreviousCard()
    })

    viewNextButton.addEventListener('click', event => {
        //when button gets clicked, call viewNextCard function
        viewNextCard()
    })
})

function showCard(index){
    let cardNum = window.cardArray[index]
    const cardDiv = document.getElementById("card-" + cardNum)
    cardDiv.style.display = "block"
}

function hideCard(index){
    let cardNum = window.cardArray[index]
    const cardDiv = document.getElementById("card-" + cardNum)
    cardDiv.style.display = "none"
}

function createArray(count) {
    cardArray = []
    for (let index = 0; index < count; index++) {
        cardArray.push(index);
    }
    return cardArray
}

function viewPreviousCard() {
    const cardArray = window.cardArray
    if (window.currentCardIndex == 0){
        return
    }
    hideCard(window.currentCardIndex)
    window.currentCardIndex--
    showCard(window.currentCardIndex)   
}

function viewNextCard() {
    const cardArray = window.cardArray
    if (window.currentCardIndex + 1 == cardArray.length){
        return
    }
    hideCard(window.currentCardIndex)
    window.currentCardIndex++ 
    showCard(window.currentCardIndex)   
}

function shuffle(array) {
    var currentIndex = array.length, temporaryValue, randomIndex;
  
    // While there remain elements to shuffle...
    while (0 !== currentIndex) {
  
      // Pick a remaining element...
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex -= 1;
  
      // And swap it with the current element.
      temporaryValue = array[currentIndex];
      array[currentIndex] = array[randomIndex];
      array[randomIndex] = temporaryValue;
    }
  
    return array;
  }