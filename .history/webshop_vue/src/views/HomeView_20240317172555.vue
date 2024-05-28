<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">Welcome to Adam's Webshop</p>
        <p class="subtitle">The best bike store online</p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="columns is-12">
        <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>
      <div>
        class="columns is-3" v-for="product in latestProducts"
        v-bind:key="product.id"
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",
  components: {},
};
</script>
