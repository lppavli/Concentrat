import { createApp } from 'vue'
import { createStore } from 'vuex'

// Create a new store instance.
const store = createStore({
  state () {
    return {
      count: 0
    }
  },
  mutations: {
    increment (state) {
      state.count++
    }
  }
})

const app = createApp({ /* your root component */ })

// Install the store instance as a plugin
app.use(store)
// import Vue from 'vue'
// import Vuex from 'vuex'
//
// Vue.use(Vuex);
//
// const state = {
//     user: null
// };
//
// const store = new Vuex.Store({
//     state,
//     getters: {
//         user: (state) => {
//             return state.user()
//         }
//     },
//     actions: {
//         user(context, user) {
//             context.commit('user', user)
//         }
//     },
//     mutations: {
//         user(state, user) {
//             state.user = user;
//         }
//     }
// });
// export default store;