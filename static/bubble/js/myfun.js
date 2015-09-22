/**
 *
 * @authors 陈小雪 (shell_chen@yeah.net)
 * @date    2015-08-21 17:02:40
 * @version $Id$
 */

function ChangeBackgroundWhite()
{
    $("#body").css("background","#ddd url(/static/bubble/images/bg.jpg) repeat top left");

}
function ChangeBackgroundBlack()
{
    $("#body").css("background", "#ddd url(/static/bubble/images/egg_shell.png) repeat top left");

}

function CloseMouseEffects() {
    demo.mousemove = function() {
    };
}

function OpenMouseEffects() {

    demo.mousemove = function() {

        var particle, theta, force, touch, max, i, j, n;

        for (i = 0, n = demo.touches.length; i < n; i++) {

            touch = demo.touches[i], max = random(1, 4);
            for (j = 0; j < max; j++) {
                demo.spawn(touch.x, touch.y);
            }

        }
    };

}
