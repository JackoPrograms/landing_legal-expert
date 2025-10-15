<template>
  <Teleport to="body">
    <transition name="modal">
      <div v-if="isOpen" class="modal-overlay" @click="handleClose">
        <div class="modal-content" @click.stop>
          <button class="modal-close" @click="handleClose">&times;</button>
          
          <h2 class="modal-title">Записаться на консультацию</h2>
          <p class="modal-subtitle">Заполните форму и мы свяжемся с вами в ближайшее время</p>

          <form @submit.prevent="handleSubmit" class="contact-form">
            <div class="form-group">
              <label for="name">Ваше имя *</label>
              <input
                id="name"
                v-model="formData.name"
                type="text"
                required
                placeholder="Иван Иванов"
                class="form-control"
              />
            </div>

            <div class="form-group">
              <label for="phone">Телефон *</label>
              <input
                id="phone"
                v-model="formData.phone"
                type="tel"
                required
                placeholder="+7 (999) 123-45-67"
                class="form-control"
              />
            </div>

            <div class="form-group">
              <label for="email">Email</label>
              <input
                id="email"
                v-model="formData.email"
                type="email"
                placeholder="example@mail.ru"
                class="form-control"
              />
            </div>

            <div class="form-group">
              <label for="service">Интересующая услуга</label>
              <select id="service" v-model="formData.service" class="form-control">
                <option value="">Выберите услугу</option>
                <option v-for="service in services" :key="service.id" :value="service.id">
                  {{ service.name }}
                </option>
              </select>
            </div>

            <div class="form-group">
              <label for="message">Сообщение</label>
              <textarea
                id="message"
                v-model="formData.message"
                rows="4"
                placeholder="Расскажите о вашей ситуации..."
                class="form-control"
              ></textarea>
            </div>

            <div v-if="error" class="alert alert-error">
              {{ error }}
            </div>

            <div v-if="success" class="alert alert-success">
              Спасибо! Ваша заявка отправлена. Мы свяжемся с вами в ближайшее время.
            </div>

            <button type="submit" class="btn btn-primary btn-block" :disabled="loading">
              {{ loading ? 'Отправка...' : 'Отправить заявку' }}
            </button>
          </form>
        </div>
      </div>
    </transition>
  </Teleport>
</template>

<script>
import { ref, reactive, watch, onMounted } from 'vue'
import { useLawyerStore } from '../stores/lawyer'
import { storeToRefs } from 'pinia'

export default {
  name: 'ContactModal',
  props: {
    isOpen: {
      type: Boolean,
      required: true,
    },
  },
  emits: ['close'],
  setup(props, { emit }) {
    const store = useLawyerStore()
    const { services } = storeToRefs(store)
    
    const formData = reactive({
      name: '',
      phone: '',
      email: '',
      service: '',
      message: '',
    })

    const loading = ref(false)
    const error = ref(null)
    const success = ref(false)

    const handleClose = () => {
      if (!loading.value) {
        emit('close')
      }
    }

    const handleSubmit = async () => {
      error.value = null
      success.value = false
      loading.value = true

      try {
        await store.sendContactRequest(formData)
        success.value = true
        
        // Reset form
        setTimeout(() => {
          formData.name = ''
          formData.phone = ''
          formData.email = ''
          formData.service = ''
          formData.message = ''
          success.value = false
          emit('close')
        }, 2000)
      } catch (err) {
        error.value = 'Ошибка отправки заявки. Попробуйте позже.'
      } finally {
        loading.value = false
      }
    }

    // Block body scroll when modal is open
    watch(() => props.isOpen, (isOpen) => {
      if (isOpen) {
        document.body.style.overflow = 'hidden'
      } else {
        document.body.style.overflow = ''
        error.value = null
        success.value = false
      }
    })

    onMounted(() => {
      if (services.value.length === 0) {
        store.fetchServices()
      }
    })

    return {
      formData,
      loading,
      error,
      success,
      services,
      handleClose,
      handleSubmit,
    }
  },
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2000;
  padding: 20px;
}

.modal-content {
  background: var(--white);
  border-radius: var(--radius-md);
  padding: 40px;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
}

.modal-close {
  position: absolute;
  top: 20px;
  right: 20px;
  background: none;
  border: none;
  font-size: 32px;
  cursor: pointer;
  color: var(--text-light);
  transition: var(--transition-fast);
}

.modal-close:hover {
  color: var(--text-dark);
}

.modal-title {
  font-size: 28px;
  margin-bottom: 10px;
  color: var(--dark-color);
}

.modal-subtitle {
  color: var(--text-light);
  margin-bottom: 30px;
}

.contact-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-weight: 600;
  color: var(--text-dark);
}

.form-control {
  padding: 12px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-sm);
  font-size: 16px;
  font-family: inherit;
  transition: var(--transition-fast);
}

.form-control:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(74, 144, 226, 0.1);
}

textarea.form-control {
  resize: vertical;
}

.alert {
  padding: 15px;
  border-radius: var(--radius-sm);
  font-size: 14px;
}

.alert-error {
  background: #fee;
  color: #c00;
  border: 1px solid #fcc;
}

.alert-success {
  background: #efe;
  color: #070;
  border: 1px solid #cfc;
}

.btn-block {
  width: 100%;
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Modal Transitions */
.modal-enter-active,
.modal-leave-active {
  transition: opacity var(--transition-normal);
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-active .modal-content,
.modal-leave-active .modal-content {
  transition: transform var(--transition-normal);
}

.modal-enter-from .modal-content,
.modal-leave-to .modal-content {
  transform: scale(0.9);
}

/* Responsive */
@media (max-width: 768px) {
  .modal-content {
    padding: 30px 20px;
  }

  .modal-title {
    font-size: 24px;
  }
}
</style>


