<template>
 <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <div class="container">
        <router-link
            :to="{ name: 'home' }"
            class="navbar-brand"
            >Flowers🌸
        </router-link>

        <div class="collapse navbar-collapse">
         <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
                <router-link
                    :to="{ name: 'home' }"
                    class="btn btn-sm btn-success"
                >Home
                </router-link>
            </li>
            <li class="nav-item mx-1">
                <router-link
                    :to="{ name: 'about' }"
                    class="btn btn-sm btn-danger"
                >About
                </router-link>
            </li>
            <li class="nav-item">
            <a class="btn btn-sm btn-outline-secondary" href="/accounts/register/">Logout</a>
            </li>
        </ul>
        <form class="form-inline my-2 my-lg-0">
            <input class="form-control mr-sm-2" type="search" placeholder="Search">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
        </div>
    </div>
</nav>
</template>

<script>
export default {
    name: "NavbarComponent"


}
</script>

<style>
    .my-navbar {
        border-bottom: 1px solid #fff;
    }
</style>