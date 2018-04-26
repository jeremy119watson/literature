
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

        if(data.current_player.can_declare){
            $scope.showMessage("You can declare the "+ data.current_player.declaration+"!", null);
        }

        $scope.cardImages = [];
        hand = data.current_player.hand;
        for(i = 0; i < hand.length; i++){
            $scope.cardImages.push('static/images/cards/'+ hand[i].imgName);
        }

        if(data.score[0] != $scope.aScore || data.score[1] != $scope.bScore) $scope.updateScore(data.score);

        if($scope.gameInfo.game_over){
            var message;
            if($scope.aScore > $scope.bScore) message = "Game over, Team A won!";
            else if($scope.aScore < $scope.bScore) message = "Game over, Team B won!";
            else team = "Game over, there's been a tie :/";
            $scope.showMessage(message, null);
            return;
        }


        document.getElementById('requestCardButton').disabled = false;

    }



    /**********************************************
     * manage highlighting of current player
     **********************************************/

    $scope.highlightPlayer = function (nextPlayer) {

        var currentPlayer = $scope.currentPlayerId;

        if (isNaN(nextPlayer)) return;                  /////////////////
        if (!Number.isInteger(nextPlayer)) return;      // validate input
        if (nextPlayer < 0 || nextPlayer > 6) return;   /////////////////

        if (currentPlayer != 0){ // unhighlight
            let box = document.getElementById(currentPlayer.toString()).style.borderBottom = "none";
        }

        currentPlayer = (currentPlayer == nextPlayer) ? 0 : nextPlayer;

        if (currentPlayer != 0){ // highlight
            document.getElementById(currentPlayer.toString()).style.borderBottom = "solid 10px rgb(255, 191, 0)";
        }

    }


    $scope.showMessage = function(message, nextFunction){
        document.getElementById('modalMessageContent').innerHTML = message;
        document.getElementById('messageModal').style.display = "block";
        document.getElementById('okButton').onclick = function () {
            document.getElementById('messageModal').style.display = "none";
            if(nextFunction != null) nextFunction();
        }
    }

    /**********************************************
     * manage requesting of a card
     **********************************************/
    
     $scope.inquiry = function(){
        
        var askee, suit, number;

        document.getElementById('requestModal').style.display='none';
        document.getElementById('requestCardButton').disabled = true;

        askee = parseInt(document.getElementById('playerSelect').value);
        if ($scope.currentPlayerId < 4) askee += 3;

        suit = parseInt(document.getElementById('suitSelect').value);
        number = parseInt(document.getElementById('numberSelect').value);


        $http.get("/game/inquiry/"+askee+"/"+suit+"/"+number)
        .then(function(response) {
            setTimeout($scope.showMessage, 500, response.data.message, $scope.next);
        });
    }

    $scope.peekHand= [];
    $scope.peek = function(playerId){

        $http.get("/game/peek/"+playerId)
        .then(function(response) {

            $scope.peekHand = [];
            hand = response.data.hand;
            for(i = 0; i < hand.length; i++){
                $scope.peekHand.push('static/images/cards/'+ hand[i].imgName);
            }
            document.getElementById('peekModal').style.display = "block";
        });
    }

});