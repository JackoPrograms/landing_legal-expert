<template>
  <header class="header" :class="{ 'scrolled-header': isScrolled }">
    <!-- Top Bar -->
    <div class="header-top">
      <div class="header-top-content">
          <div class="header-contacts">
            <a href="tel:+79220229482" class="header-contact-item">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M13.3332 0.833252H6.6665C5.28317 0.833252 4.1665 1.94992 4.1665 3.33325V16.6666C4.1665 18.0499 5.28317 19.1666 6.6665 19.1666H13.3332C14.7165 19.1666 15.8332 18.0499 15.8332 16.6666V3.33325C15.8332 1.94992 14.7165 0.833252 13.3332 0.833252ZM14.1665 14.9999H5.83317V3.33325H14.1665V14.9999ZM11.6665 17.4999H8.33317V16.6666H11.6665V17.4999Z" fill="#4F8FF0"/>
              </svg>
              +7 (922) 022-94-82
            </a>
            <a href="mailto:janis62@yahoo.com" class="header-contact-item">
              <svg width="18" height="14" viewBox="0 0 18 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.33317 13.6666C1.87484 13.6666 1.48234 13.5033 1.15567 13.1766C0.829005 12.8499 0.66595 12.4577 0.666505 11.9999V1.99992C0.666505 1.54159 0.829839 1.14909 1.15651 0.82242C1.48317 0.495753 1.87539 0.332698 2.33317 0.333253H15.6665C16.1248 0.333253 16.5173 0.496587 16.844 0.823253C17.1707 1.14992 17.3337 1.54214 17.3332 1.99992V11.9999C17.3332 12.4583 17.1698 12.8508 16.8432 13.1774C16.5165 13.5041 16.1243 13.6671 15.6665 13.6666H2.33317ZM8.99984 7.83325L2.33317 3.66659V11.9999H15.6665V3.66659L8.99984 7.83325ZM8.99984 6.16659L15.6665 1.99992H2.33317L8.99984 6.16659ZM2.33317 3.66659V1.99992V11.9999V3.66659Z" fill="#4F8FF0"/>
              </svg>
              janis62@yahoo.com
            </a>
          </div>
          <button class="btn-call" @click="$emit('open-modal')">
            Заказать звонок
          </button>
        </div>
      </div>

    <!-- Main Header Wrapper -->
    <div class="header-main-wrapper" :class="{ 'scrolled': isScrolled }">
      <div class="header-main">
        <div class="header-main-container">
          <div class="header-logo">
            <h1>{{ companyInfo?.company_name || 'ПРАВОЗАЩИТНИК' }}</h1>
            <p class="header-logo-subtitle">юридическая компания</p>
          </div>

          <!-- Desktop Menu -->
          <nav class="header-nav desktop-nav">
            <a href="#services" class="nav-link">Услуги</a>
            <a href="#about" class="nav-link active">О компании</a>
            <a href="#lawyers" class="nav-link">Наши юристы</a>
            <a href="#reviews" class="nav-link">Отзывы</a>
            <a href="#articles" class="nav-link">Полезное</a>
          </nav>

          <!-- Mobile Menu Button -->
          <button class="mobile-menu-btn" @click="mobileMenuOpen = !mobileMenuOpen">
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Menu -->
    <transition name="slide">
      <div v-if="mobileMenuOpen" class="mobile-menu">
        <nav class="mobile-nav">
          <a href="#services" class="nav-link" @click="mobileMenuOpen = false">Услуги</a>
          <a href="#about" class="nav-link" @click="mobileMenuOpen = false">О компании</a>
          <a href="#lawyers" class="nav-link" @click="mobileMenuOpen = false">Наши юристы</a>
          <a href="#reviews" class="nav-link" @click="mobileMenuOpen = false">Отзывы</a>
          <a href="#articles" class="nav-link" @click="mobileMenuOpen = false">Полезное</a>
          <button class="btn btn-primary" @click="handleMobileContact">
            Записаться онлайн
          </button>
        </nav>
      </div>
    </transition>
  </header>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue'
import { useLawyerStore } from '../stores/lawyer'
import { storeToRefs } from 'pinia'

export default {
  name: 'AppHeader',
  emits: ['open-modal'],
  setup(props, { emit }) {
    const store = useLawyerStore()
    const { companyInfo } = storeToRefs(store)
    const mobileMenuOpen = ref(false)
    const isScrolled = ref(false)

    const handleScroll = () => {
      isScrolled.value = window.scrollY > 52
    }

    onMounted(() => {
      if (!companyInfo.value) {
        store.fetchCompanyInfo()
      }
      window.addEventListener('scroll', handleScroll)
    })

    onUnmounted(() => {
      window.removeEventListener('scroll', handleScroll)
    })

    const handleMobileContact = () => {
      mobileMenuOpen.value = false
      emit('open-modal')
    }

    return {
      companyInfo,
      mobileMenuOpen,
      isScrolled,
      handleMobileContact,
    }
  },
}
</script>

<style scoped>
.header {
  position: relative;
  z-index: 1000;
}

.header-top {
  background: #010101;
  color: #FFFFFF;
  padding: 0;
  height: 52px;
  display: flex;
  align-items: center;
}

.header-top-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100%;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.header-contacts {
  display: flex;
  gap: 30px;
  align-items: center;
}

.header-contact-item {
  color: #FFFFFF;
  font-size: 14px;
  font-family: 'Nunito Sans', sans-serif;
  font-weight: 400;
  display: flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  transition: var(--transition-fast);
}

.header-contact-item:hover {
  color: #4F8FF0;
}

.header-contact-item svg {
  flex-shrink: 0;
}

.btn-call {
  background: none;
  border: none;
  color: #4F8FF0;
  font-size: 14px;
  font-family: 'Nunito Sans', sans-serif;
  font-weight: 400;
  cursor: pointer;
  transition: var(--transition-fast);
  padding: 0;
}

.btn-call:hover {
  color: #FFFFFF;
}

  .header-main-wrapper {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    width: 100%;
    height: 162px; /* 50px (top bar) + 112px (main menu) */
    z-index: 1000;
    transition: all 0.3s ease;
  }

  .header-main-wrapper.scrolled {
    position: fixed;
    top: 0;
  }

  .header-main-wrapper.scrolled .header-main {
    top: 0;
    height: 92px; /* 112px - 20px = 92px */
  }

  .header-main {
    padding: 0;
    background: rgba(1, 1, 1, 0.76);
    backdrop-filter: blur(10px);
    position: absolute;
    top: 50px;
    left: 0;
    right: 0;
    width: 100%;
    height: 112px;
    z-index: 1001;
    display: flex;
    align-items: center;
    justify-content: center;
  }

.header-main-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  position: relative;
}


.header-logo h1 {
  font-size: 24px;
  font-weight: 800;
  color: #4F8FF0;
  margin: 0;
}

.header-logo-subtitle {
  font-size: 14px;
  font-weight: 400;
  color: #FFFFFF;
  margin: 0;
  margin-top: -5px;
}

.header-logo {
  display: flex;
  flex-direction: column;
}

.header-nav {
  display: flex;
  gap: 30px;
  align-items: center;
}

.nav-link {
  color: #FFFFFF;
  font-weight: 600;
  position: relative;
}

.nav-link:hover {
  color: var(--primary-color);
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--primary-color);
  transition: var(--transition-fast);
}

.nav-link:hover::after,
.nav-link.active::after {
  width: 100%;
}

.mobile-menu-btn {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 5px;
}

.mobile-menu-btn span {
  width: 25px;
  height: 3px;
  background: #FFFFFF;
  transition: var(--transition-fast);
}

  .mobile-menu {
    position: fixed;
    left: 0;
    right: 0;
    background: var(--white);
    box-shadow: var(--shadow-lg);
    z-index: 999;
    transition: top 0.3s ease;
  }

  /* Mobile menu when header is NOT scrolled */
  .header:not(.scrolled-header) .mobile-menu {
    top: 162px; /* 52px (top bar) + 112px (main menu) */
  }

  /* Mobile menu when header IS scrolled */
  .header.scrolled-header .mobile-menu {
    top: 92px; /* Height of compressed main menu (112px - 20px) */
  }

.mobile-nav {
  display: flex;
  flex-direction: column;
  padding: 20px;
  gap: 15px;
}

.mobile-nav .nav-link {
  padding: 10px;
  border-bottom: 1px solid var(--border-color);
}

.mobile-nav .btn {
  margin-top: 10px;
}

/* Transitions */
.slide-enter-active,
.slide-leave-active {
  transition: var(--transition-normal);
}

.slide-enter-from,
.slide-leave-to {
  transform: translateY(-100%);
  opacity: 0;
}

/* Tablet Styles (835px and below) */
@media (max-width: 835px) {
  .desktop-nav {
    display: none;
  }

  .mobile-menu-btn {
    display: flex;
  }

  .header-main-wrapper {
    height: 136px; /* 52px (top bar) + 84px (main menu) */
  }

  .header-top {
    height: 52px;
  }

  .header-main {
    top: 52px;
    height: 84px;
  }

  .header-main-wrapper.scrolled .header-main {
    height: 64px; /* 84px - 20px = 64px */
  }

  .header-top-content {
    max-width: 100%;
    padding: 0 15px;
  }

  .header-main-container {
    max-width: 100%;
    padding: 0 15px;
  }

  .header-contacts {
    gap: 20px;
  }

  .header-contact-item {
    font-size: 12px;
  }

  .header-logo h1 {
    font-size: 20px;
  }

  .header-logo-subtitle {
    font-size: 12px;
  }

  .btn-call {
    font-size: 12px;
  }

  /* Mobile menu for tablet */
  .header:not(.scrolled-header) .mobile-menu {
    top: 136px; /* 52px (top bar) + 84px (main menu) */
  }

  .header.scrolled-header .mobile-menu {
    top: 64px; /* Height of compressed main menu (84px - 20px) */
  }
}

/* Hide email on smaller screens (420px and below) */
@media (max-width: 420px) {
  /* Hide email - show only phone */
  .header-contact-item:last-child {
    display: none;
  }
}

/* Mobile Styles (390px and below) */
@media (max-width: 390px) {
  .header-main-wrapper {
    height: 136px; /* 52px (top bar) + 84px (main menu) */
  }

  .header-top {
    height: 52px;
  }

  .header-main {
    top: 52px;
    height: 84px;
  }

  .header-main-wrapper.scrolled .header-main {
    height: 64px; /* 84px - 20px = 64px */
  }

  .header-top-content {
    flex-direction: row;
    justify-content: space-between;
    gap: 10px;
    padding: 0 10px;
  }

  .header-main-container {
    padding: 0 10px;
  }

  .header-contacts {
    flex-direction: row;
    gap: 10px;
  }

  .header-contact-item {
    font-size: 11px;
  }

  .header-logo h1 {
    font-size: 18px;
  }

  .header-logo-subtitle {
    font-size: 11px;
  }

  .btn-call {
    font-size: 11px;
  }

  /* Mobile menu for mobile */
  .header:not(.scrolled-header) .mobile-menu {
    top: 136px; /* 52px (top bar) + 84px (main menu) */
  }

  .header.scrolled-header .mobile-menu {
    top: 64px; /* Height of compressed main menu (84px - 20px) */
  }
}
</style>


