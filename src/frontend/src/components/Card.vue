<template>
  <div class="card" @click="flipped = !flipped">
    <div class="card-content" :class="{ flipped: flipped }">
      <div class="front">
        <slot name="front">
          Front face
        </slot>
      </div>
      <div class="back">
        <slot name="back">
          Back face
        </slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      flipped: false
    }
  }
}
</script>

<style scoped>
.card {
  background-color: transparent;
  width: 400px;
  height: 150px;
  border: 1px solid #f1f1f1;
  perspective: 1000px; /* 3D effect */
}
.card-content {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.8s;
  transform-style: preserve-3d;
}
.flipped {
  transform: rotateY(180deg);
}

.front, .back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}
.front {
  background-color: #bbb;
  color: black;
}

.back {
  background-color: dodgerblue;
  color: white;
  transform: rotateY(180deg);
}
</style>
