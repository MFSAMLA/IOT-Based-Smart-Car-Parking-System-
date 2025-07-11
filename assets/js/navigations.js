// Initialize Bootstrap tooltips
document.addEventListener('DOMContentLoaded', function () {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.forEach(function (tooltipTriggerEl) {
      new bootstrap.Tooltip(tooltipTriggerEl);
    });
  });
  
  // Toggle active class for sidebar buttons
  document.querySelectorAll('.sidebar-btn').forEach(btn => {
    btn.addEventListener('click', function () {
      document.querySelector('.sidebar-btn.active').classList.remove('active');
      this.classList.add('active');
    });
  });
  