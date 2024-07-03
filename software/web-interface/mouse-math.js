const cursorBox = document.getElementById('cursor-box');
const cursorPos = cursorBox.getBoundingClientRect();
const container = document.getElementById('container');
const max_x = container.offsetWidth;
const max_y = container.offsetHeight;
const cursor_width = cursorBox.offsetWidth;
const cursor_height = cursorBox.offsetHeight;
const init_x = cursorPos.left + (cursorBox.offsetWidth / 2);
const init_y = cursorPos.top - (cursorBox.offsetHeight / 2) + 8; // 8 magic number may be due to padding

let x = init_x;
let y = init_y;
let prev_cursor_x = x;
let prev_cursor_y = y;

console.log(x, y);

const moveCursor = (x, y) => {
  if (x > max_x || y > max_y) return;
  if (x < 0 || y < 0) return;

  cursorBox.style.left = init_x + 'px';
  cursorBox.style.top = init_y + 'px';
}

const resetCursor = () => {
  moveCursor(init_x, init_y);
}

const round = (val) => Math.round(val * 100) / 100;

// assumes an equilateral triangle layout where the points are treated as: top, left, right
// top, left, right
// measured in inches
const updateCursor = (data) => {
  if (data.includes(',')) {
    const sensorVals = data.split(',');
    const topSensorVal = parseFloat(sensorVals[0]);
    const leftSensorVal = parseFloat(sensorVals[1]);
    const rightSensorVal = parseFloat(sensorVals[2]);

    // finger in area
    if (topSensorVal < 6 || leftSensorVal < 6 || rightSensorVal < 6) {
      console.log('finger detected', [topSensorVal, leftSensorVal, rightSensorVal]);
      cursorBox.style.left = leftSensorVal + 'px';
      cursorBox.style.top = topSensorVal + 'px';

      const ts_y = round(topSensorVal);
      const degToRad = ((60 * Math.PI) / 180);
      const ls_x = round(leftSensorVal * Math.cos(degToRad));
      const ls_y = round(leftSensorVal * Math.sin(degToRad));
      const rs_x = round(rightSensorVal * Math.cos(degToRad));
      const rs_y = round(rightSensorVal * Math.sin(degToRad));

      console.log(rs_x - ls_x);
      let xDiff = rs_x - ls_x;

      prev_cursor_x += xDiff * 10;

      console.log('prev', prev_cursor_x);

      moveCursor(prev_cursor_x, 0);
    } else {
      prev_cursor_x = init_x;
      prev_cursor_y = init_y;
      resetCursor();
    }
  } else {
    console.error('invalid data');
  }
}