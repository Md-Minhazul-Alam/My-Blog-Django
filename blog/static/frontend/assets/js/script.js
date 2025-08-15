function toggleMobileMenu(){
    const sidebar = document.getElementById('mobileSidebar');
    const overlay = document.querySelector('.mobile-overlay');
    
    sidebar.classList.add('active');
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
}
function closeMobileMenu(){
    const sidebar = document.getElementById('mobileSidebar');
    const overlay = document.querySelector('.mobile-overlay');
    
    sidebar.classList.remove('active');
    overlay.classList.remove('active');
    document.body.style.overflow = 'auto';
}