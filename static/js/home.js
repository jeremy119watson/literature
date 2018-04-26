
var app = angular.module("Literature",[]);

app.controller("GameController", function($scope, $http){

    // index | color
    // -------------------------
    //     0 | A main
    //     1 | A highlight
    //     2 | B main
    //     3 | B highlight
    //
    let teamColors = ['rgb(0, 145, 225)', 'rgb(0, 165, 235)', 'rgb(0, 135, 10)', 'rgb(0, 155, 20)'];

    $scope.currentPlayer;
    $scope.currentPlayerId = 0;
    $scope.gameInfo;
    $scope.cardImages = [];

    /**********************************************
     * manage display of score
     **********************************************/

    $scope.aScore = 0;
    $scope.bScore = 0;

    $scope.updateScore = function(score){
        $scope.aScore = score[0];
        $scope.bScore = score[1];
        document.getElementById('aSco').innerHTML = $scope.aScore.toString();
        document.getElementById('bSco').innerHTML = $scope.bScore.toString();
    }

    $scope.startGame = function(){
        document.getElementById('startGrid').style.display = "none";
        document.getElementById('gameHome').style.display = "grid";
  
        $http.get("/game/start")
        .then(function(response) {
            $scope.loadTurn(response.data);
        });
        

    }

    $scope.inquiry = function(askee, suit, number){
        // hide selection modal

        $http.get("/game/inquiry/askee,suit,number")
        .then(function(response) {
            $scope.displayMessage(response.data);
        });
    }

    $scope.displayMessage = function(data){
        // show message
        // 
    }

    $scope.next = function(){
        $http.get("/game/json")
        .then(function(response) {
            $scope.loadTurn(response.data);
        });
    }

    $scope.loadTurn = function(data){

        let newPlayer = $scope.currentPlayerId != data.current_player.id ? true : false;
       
        if(newPlayer) $scope.highlightPlayer(data.current_player.id);

        $scope.currentPlayer = data.current_player;
        $scope.currentPlayerId = data.current_player.id;

        $scope.gameInfo = data;

        hand = data.current_player.hand;
        for(i = 0; i < hand.length; i++){
            console.log("hello");
            $scope.cardImages.push('static/images/cards/'+ hand[i].imgName);
        }
        console.log($scope.cardImages);

        if(data.score[0] != $scope.aScore || data.score[1] != $scope.bScore) $scope.updateScore(data.score);

        if($scope.gameInfo.game_over){
            // display game over
            // exit function
        }


        if($scope.currentPlayer.can_declare){
            // show delcare button and info
        } else {
            // normal turn
        }

    }



    /**********************************************
     * manage highlighting of current player
     **********************************************/

    $scope.highlightPlayer = function (nextPlayer) {

        var currentPlayer = $scope.currentPlayerId;

        if (isNaN(nextPlayer)) return;                  /////////////////
        if (!Number.isInteger(nextPlayer)) return;      // validate input
        if (nextPlayer < 0 || nextPlayer > 6) return;   /////////////////
        
        let unHighlight = function () {
            let box = document.getElementById(currentPlayer.toString());
            if (box.style.color == "white") return;
            box.style.backgroundColor = teamColors[currentPlayer > 3 ? 2 : 0]
            box.style.color = "white";
        }

        let highlight = function () {
            let box = document.getElementById(nextPlayer.toString());
            if (box.style.color == "black") return;
            box.style.backgroundColor = "rgb(255, 191, 0)";
            box.style.color = "black";
        }

        if (currentPlayer != 0) unHighlight();
        currentPlayer = (currentPlayer == nextPlayer) ? 0 : nextPlayer;
        if (currentPlayer != 0) highlight();
    }
});