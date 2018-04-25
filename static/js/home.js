
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

    /**********************************************
     * manage display of score
     **********************************************/

    $scope.aScore = 0;
    $scope.bScore = 0;

    $scope.updateScore = function(a,b){
        $scope.aScore += a;
        $scope.bScore += b;
        document.getElementById('aSco').innerHTML = $scope.aScore.toString();
        document.getElementById('bSco').innerHTML = $scope.bScore.toString();
    }

    $scope.startGame = function(){
        document.getElementById('startButton').style.display = "none";
        $http.get("/game/start")
        .then(function(response) {
            $scope.highlightPlayer(response.data.current_player);
        });
        document.getElementById('nextButton').style.display = "block";
    }

    $scope.nextPlayer = function(){
        $http.get("/game/next")
        .then(function(response) {
            $scope.highlightPlayer(response.data.current_player);
        });
    }


    /**********************************************
     * manage highlighting of current player
     **********************************************/

    let currentPlayer = 0;

    $scope.highlightPlayer = function (nextPlayer) {
        if (isNaN(nextPlayer)) return;                  /////////////////
        if (!Number.isInteger(nextPlayer)) return;      // validate input
        if (nextPlayer < 0 || nextPlayer > 6) return;   /////////////////
        
        let unHighlight = function () {
            let box = document.getElementById(currentPlayer.toString());
            if (box.style.color == "white") return;
            box.style.backgroundColor = teamColors[currentPlayer > 3 ? 3 : 1]
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