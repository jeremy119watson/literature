var canWidth;
var canHeight;
var parent;

function preload() {
    // load up card pictures?
}

function setup(){
    parent = select('#player-hand-canvas')
    calculateSize();

    playerHandCanvas = createCanvas(canWidth,canHeight);
    playerHandCanvas.parent(parent);

    background(134);
}

function draw(){
    background(134);
}

function windowResized() {
    calculateSize();
    resizeCanvas(canWidth, canHeight);
}

function calculateSize(){
    canWidth = windowWidth > 565 ? 565 : windowWidth-20;
    canHeight = parent.height - 20;
    console.log(canWidth);
    console.log(canHeight);
}