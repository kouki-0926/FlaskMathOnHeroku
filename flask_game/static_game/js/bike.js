var t = 0;
var size = 10;
var speed = 0;
var playing = true;
var grounded = 0;
var k = { ArrowUp: 0, ArrowDown: 0, ArrowLeft: 0, ArrowRight: 0 };

// canvas 生成
var c = document.createElement("canvas");
var ctx = c.getContext("2d");
var parentDiv = document.getElementById("parent-div");
var title = document.getElementById("title");
parentDiv.insertBefore(c, title.nextSibling);
c.classList.add('display-none');


// 画面生成のパラメータ生成
var perm = [];
while (perm.length < 255) {
    while (perm.includes(val = Math.floor(Math.random() * 255)));
    perm.push(val);
}

var lerp = (a, b, t) => a + (b - a) * (1 - Math.cos(t * Math.PI)) / 2;

var noise = x => {
    x = x * 0.01 % 255;
    return lerp(perm[Math.floor(x)], perm[Math.ceil(x)], x - Math.floor(x));
}


// player生成
var player = new function () {
    this.x = c.width / 2;
    this.y = 0;
    this.ySpeed = 0;
    this.rSpeed = 0;
    this.rot = 0;
    this.img = new Image();
    this.img.src = "static_game/images/moto.png";

    this.draw = function () {
        // 乱数生成
        var p1 = c.height - noise(t + this.x) * 0.25;
        var p2 = c.height - noise(t + 5 + this.x) * 0.25;

        // 縦移動のスピードの更新
        if (p1 - size > this.y) {
            this.ySpeed += 0.1;
        } else {
            this.ySpeed -= this.y - (p1 - size);
            this.y = p1 - size;
            grounded = 1;
        }
        this.y += this.ySpeed;

        // 回転回転のスピードの更新
        var angle = Math.atan2((p2 - 10) - this.y, 5);
        if (grounded && playing) {
            this.rot -= (this.rot - angle) * 0.5;
            this.rSpeed = this.rSpeed - (angle - this.rot);
        }
        this.rSpeed += (k.ArrowRight - k.ArrowLeft) * 0.5;
        this.rot += this.rSpeed * 0.01;

        // 回転しすぎを修正
        if (this.rot > Math.PI) this.rot = -Math.PI;
        if (this.rot < -Math.PI) this.rot = Math.PI;

        // gameover判定
        if (!playing || grounded && Math.abs(this.rot) > Math.PI * 0.8) {
            playing = false;
            this.rSpeed = 15;
            k.ArrowUp = 1;
            this.x -= speed * 15;
        }


        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(this.rot);
        ctx.drawImage(this.img, -15, -15, 30, 30);
        ctx.restore();
    }
}

function loop() {
    if (playing) {
        speed -= (speed - (k.ArrowUp - k.ArrowDown)) * 0.1;
        t += 10 * speed;
    } else {
        t += 30;
    }

    ctx.fillStyle = "#19f";
    ctx.fillRect(0, 0, c.width, c.height);
    ctx.fillStyle = "black";
    ctx.beginPath();

    ctx.moveTo(0, c.height);
    for (var i = 0; i < c.width; i++) {
        ctx.lineTo(i, c.height - noise(t + i) * 0.25);
    }
    ctx.lineTo(c.width, c.height);
    ctx.fill();

    player.draw();
    requestAnimationFrame(loop);
}

// 押されたkey判定
onkeydown = d => k[d.key] = 1;
onkeyup = d => k[d.key] = 0;

loop();