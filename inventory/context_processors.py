def sidebar_categories(request):
    icon_map = {
        'Desktop': 'bi bi-pc-display',
        'Laptop': 'bi bi-laptop',
        'Printer': 'bi bi-printer',
        'Security': 'bi bi-shield-lock',
        'Network Devices': 'bi bi-router',
        'Electrical Devices': 'bi bi-lightning-charge',
        'Tools': 'bi bi-tools',
        'Telephony': 'bi bi-telephone',
        'Display': 'bi bi-display',
    }
    cats = [{'name': k, 'icon': v} for k, v in icon_map.items()]
    return {
        'sidebar_categories': cats,
        'current_category': request.resolver_match.kwargs.get('category', '') if hasattr(request, 'resolver_match') and request.resolver_match else '',
    }
