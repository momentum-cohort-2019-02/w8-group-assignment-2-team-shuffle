document.addEventListener('DOMContentLoaded', function (){
    const viewPreviousButton = document.getElementById('view-previous')
    const viewNextButton = document.getElementById('view-next')
    const cardCount = document.getElementById('card-count')
    
    cardArray = createArray(cardCount.innerText)
    shuffledCardArray = shuffle(cardArray)
    // console.log(shuffledCardArray)

    viewPreviousButton.addEventListener('click', event => {
        //when button gets clicked, call viewPreviousCard function
        viewPreviousCard()
    })

    viewNextButton.addEventListener('click', event => {
        //when button gets clicked, call viewNextCard function
        viewNextCard()
    })
})

function createArray(count) {
    cardArray = []
    for (let index = 0; index < count; index++) {
        cardArray.push(index);
    }
    return cardArray
}

function viewPreviousCard() {

}

function viewNextCard() {

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