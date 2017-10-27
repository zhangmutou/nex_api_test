from nex_b import (RemainTest, RoleTest, UserTest,
						ChargeTest, ConsumeTest, DspTest,
						ApplyTest, ApproveTest, AuditingTest,
						IndustryTest, InvoceTest, PositionTest,
)

from nex_session import NexSession

cases = []

Dsp = None
User = None
Role = None
Apply = None
Remain = None
Charge = None
Invoce = None
Consume = None
Approve = None
Auditing = None
Industry = None
Position = None
# case
# id
# name
# desc
# url
# method
# role 	1:superadmin 2:admin 3:normal 4:none
# exception
# interface 	1:user 2:role 3:dsp 4:apply 5:remain 6:charge 7:invoce 8:consume
#               9:approve 10:auditing 11:industry 12:position

def generate_test(interface_list, test_cases):
	generate_test_class(interface_list)
	for case in test_cases:
		generate_test_func(case)

	return cases

def generate_test_class(interface_list):
	if 1 in interface_list: _generate_user_class()
	if 2 in interface_list: _generate_role_class()
	if 3 in interface_list: _generate_dsp_class()
	if 4 in interface_list: _generate_apply_class()
	if 5 in interface_list: _generate_remain_class()
	if 6 in interface_list: _generate_charge_class()
	if 7 in interface_list: _generate_invoce_class()
	if 8 in interface_list: _generate_consume_class()
	if 9 in interface_list: _generate_approve_class()
	if 10 in interface_list: _generate_auditing_class()
	if 11 in interface_list: _generate_industry_class()
	if 12 in interface_list: _generate_position_class()

def generate_test_func(case):
	interface = case['interface']
	if interface == 1: setattr(User, 'test_{}'.format(case['name']), User.add_test_func(case))
	if interface == 2: setattr(Role, 'test_{}'.format(case['name']), Role.add_test_func(case))
	if interface == 3: setattr(Dsp, 'test_{}'.format(case['name']), Dsp.add_test_func(case))
	if interface == 4: setattr(Apply, 'test_{}'.format(case['name']), Apply.add_test_func(case))
	if interface == 5: setattr(Remain, 'test_{}'.format(case['name']), Remain.add_test_func(case))
	if interface == 6: setattr(Charge, 'test_{}'.format(case['name']), Charge.add_test_func(case))
	if interface == 7: setattr(Invoce, 'test_{}'.format(case['name']), Invoce.add_test_func(case))
	if interface == 8: setattr(Consume, 'test_{}'.format(case['name']), Consume.add_test_func(case))
	if interface == 9: setattr(Approve, 'test_{}'.format(case['name']), Approve.add_test_func(case))
	if interface == 10: setattr(Auditing, 'test_{}'.format(case['name']), Auditing.add_test_func(case))
	if interface == 11: setattr(Industry, 'test_{}'.format(case['name']), Industry.add_test_func(case))
	if interface == 12: setattr(Position, 'test_{}'.format(case['name']), Position.add_test_func(case))

def _generate_user_class():
	global User
	User = type('User', (UserTest,), {})
	cases.append(User)

def _generate_role_class():
	global Role
	Role = type('Role', (RoleTest,), {})
	cases.append(Role)

def _generate_dsp_class():
	global Dsp
	Dsp = type('Dsp', (DspTest,), {})
	cases.append(Dsp)

def _generate_apply_class():
	global Apply
	Apply = type('Apply', (ApplyTest,), {})
	cases.append(Apply)

def _generate_remain_class():
	global Remain
	Remain = type('Remain', (RemainTest,), {})
	cases.append(Remain)

def _generate_charge_class():
	global Charge
	Charge = type('Charge', (ChargeTest,), {})
	cases.append(Charge)

def _generate_invoce_class():
	global Invoce
	Invoce = type('Invoce', (InvoceTest,), {})
	cases.append(Invoce)

def _generate_consume_class():
	global Consume
	Consume = type('Consume', (ConsumeTest,), {})
	cases.append(Consume)

def _generate_approve_class():
	global Approve
	Approve = type('Approve', (ApproveTest,), {})
	cases.append(Approve)

def _generate_auditing_class():
	global Auditing
	Auditing = type('Auditing', (AuditingTest,), {})
	cases.append(Auditing)

def _generate_industry_class():
	global Industry
	Industry = type('Industry', (IndustryTest,), {})
	cases.append(Industry)

def _generate_position_class():
	global Position
	Position = type('Position', (PositionTest,), {})
	cases.append(Position)

