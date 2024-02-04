from django.contrib import messages
from django.shortcuts import redirect, render
from fin.models import *
import random
import array

# unique random transaction id generator


def transaction_id_generator():
    # maximum length of password needed
    # this can be changed to suit your password length

    MAX_LEN = 10

    # declare arrays of the character that we need in out password
    # Represented as chars to enable easy string concatenation
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '%', '&', '$']

    # combines all the character arrays above to form one array
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    # randomly select at least one character from each character set above
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    # combine the character randomly selected above
    # at this stage, the password contains only 4 characters but
    # we want a 12-character password
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    # now that we are sure we have at least one character from each
    # set of characters, we fill the rest of
    # the password length by selecting randomly from the combined
    # list of character above.
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        # convert temporary password into array and shuffle to
        # prevent it from having a consistent pattern
        # where the beginning of the password is predictable
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    transaction_id = ""
    for x in temp_pass_list:
        transaction_id = transaction_id + x

    # print out password
    return transaction_id


# funtion that generate account ID
def account_id_generator():
    account_id = random.randint(1000000000, 10000000000)
    return account_id


def get_transfer(request):
    if request.method == "POST":
        account_id = request.POST['accountid']
        amount = request.POST['amount']
        print(account_id, amount)

        revenues = Revenue.objects.get(id=1)
        gas_fee = revenues.gas_fee
        service_charge = float(amount)*(gas_fee/100)

        try:
            receiver_account = BankAccount.objects.get(
                account_id=account_id)
            receiver = receiver_account.user.username
            sender_account = BankAccount.objects.get(user=request.user)
            transfer = Transfer.objects.create(
                account_id=account_id, amount=amount)

            transfer.save()

            ledger = Ledger.objects.create(sender=sender_account.user.username,
                                           receiver=receiver_account.user.username,
                                           amount=amount,
                                           transaction_id=transaction_id_generator())

            ledger.save()

            # balance system
            try:
                sender_account.balance = sender_account.balance - \
                    float(amount) - float(service_charge)

                receiver_account.balance = receiver_account.balance + \
                    float(amount)

                sender_account.save()
                receiver_account.save()

                revenues.revenue += float(service_charge)
                revenues.save()

                messages.info(
                    request, 'You successfully sent {}$ to {}.'.format(amount, receiver))

            except:
                messages.info(request, 'Balance not updated')

        except:
            messages.info(request, 'No User Found')
        return redirect('transfer')


def get_transaction(request):
    transactions = Ledger.objects.filter(
        sender=request.user.username) or Ledger.objects.filter(receiver=request.user.username)
    count = transactions.count()
    no_tran = ''

    if not transactions:
        no_tran = 'No transaction'

    return {'transactions': transactions, 'count': count, 'no_tran': no_tran}
