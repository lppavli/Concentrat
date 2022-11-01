import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login'
import MaterialsView from "@/views/MaterialsView";
import addView from "@/views/AddView";
import Logout from '../views/Logout'
import Report from '../views/Report'
const routes = [
  {
    path: '/',
    name: 'Materials',
    component: MaterialsView
  },
    {
    path: '/login',
    name: 'Login',
    component: Login
  },
        {
    path: '/logout',
    name: 'Logout',
    component: Logout
  },
        {
    path: '/add',
    name: 'add',
    component: addView
  },
     {
    path: '/report',
    name: 'Report',
    component: Report
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
