/* ============================================
   SMART HOSTEL - JAVASCRIPT UTILITIES
   ============================================ */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Add smooth scroll behavior
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// Day-wise menu filter function
function filterMenuByDay(selectedDate) {
    const menuItems = document.querySelectorAll('[data-menu-date]');
    menuItems.forEach(item => {
        if (item.getAttribute('data-menu-date') === selectedDate) {
            item.style.display = 'block';
            item.classList.add('fade-in');
        } else {
            item.style.display = 'none';
        }
    });
}

// Payment calculation
function calculateRemaining() {
    const totalInput = document.querySelector('input[name="amount"]');
    const paidInput = document.querySelector('input[name="paid_amount"]');
    const remainingDisplay = document.getElementById('remainingAmount');

    if (totalInput && paidInput && remainingDisplay) {
        const total = parseFloat(totalInput.value) || 0;
        const paid = parseFloat(paidInput.value) || 0;
        const remaining = Math.max(0, total - paid);
        remainingDisplay.textContent = '₹' + remaining.toFixed(0);
    }
}

// Sort complaints by status
function sortComplaints(status) {
    const complaints = document.querySelectorAll('[data-complaint-status]');
    complaints.forEach(complaint => {
        if (status === 'all' || complaint.getAttribute('data-complaint-status') === status) {
            complaint.style.display = 'block';
        } else {
            complaint.style.display = 'none';
        }
    });
}

// Add smooth animations on page load
function animateElements() {
    const elements = document.querySelectorAll('.card, .btn, .alert');
    elements.forEach((el, index) => {
        el.style.animation = `slideIn 0.3s ease-out ${index * 0.05}s forwards`;
        el.style.opacity = '0';
    });
}

// Export functions for use in templates
window.filterMenuByDay = filterMenuByDay;
window.sortComplaints = sortComplaints;
window.calculateRemaining = calculateRemaining;
window.animateElements = animateElements;
