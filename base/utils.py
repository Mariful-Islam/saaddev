
from django.db.models import Q
from base.models import Contact


def get_mail(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    contact = Contact.objects.filter(Q(username__icontains=q) |
                                     Q(email__icontains=q) |
                                     Q(message__icontains=q) |
                                     Q(category__icontains=q)
                                     )

    contacts = Contact.objects.all()
    all_count = contacts.count()
    count = contact.count()
    inbox_count = Contact.objects.filter(category=1).count()
    draft_count = Contact.objects.filter(category=2).count()
    sent_count = Contact.objects.filter(category=3).count()
    spam_count = Contact.objects.filter(category=4).count()

    context = {
        "contact": contact,
        "contacts": contacts,
        "all_count": all_count,
        "count": count,
        "inbox_count": inbox_count,
        "draft_count": draft_count,
        "sent_count": sent_count,
        "spam_count": spam_count
    }

    return context

#contact, contacts, all_count, count, inbox_count, draft_count, sent_count, spam_count
