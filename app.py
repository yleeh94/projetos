import streamlit as st
import json
import gspread
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os.path
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
import schedule
import getpass
import pickle
import datetime
import smtplib
import email.message
import datetime




{
    "bolhas": [
"INCIDENTS_READ",
"FBM_OUTBOUND_PROBLEM_SOLVER",
"FBM_MWH_OUTBOUND_PICKING_OPERATOR",
"FBM_OUTBOUND_PACKING_OPERATOR",
"FBM_INBOUND_CHECK_IN_OPERATOR",
"FBM_INBOUND_PUT_AWAY_OPERATOR",
"SHPBO_FRAUD_PREVENTION",
"FOS_TEAM_LEADER",
"FBM_MULTIPLICATOR",
"FBM_MWH_OUTBOUND_PROBLEM_SOLVER",
"FBM_RL_CYCLE_COUNT_OPERATOR",
"FBM_INVENTORY_OPERATOR",
"FBM_OUTBOUND_DISPATCH_OPERATOR",
"FBM_OUTBOUND_PICKING_OPERATOR",
"FOS_OPERATOR_EXPEDITION",
"FBM_INBOUND_SUPERVISOR",
"FBM_INBOUND_CHECK_IN_OPERATOR_EXPERT",
"FBM_MWH_OUTBOUND_DISPATCH_OPERATOR_EXPERT",
"FBM_RC_CHECK_IN_OPERATOR",
"FBM_WITHDRAWAL_PICKING_OPERATOR",
"FBM_RC_PICK_TO_MOVABLE_OPERATOR",
"FBM_MWH_INBOUND_PUT_AWAY_OPERATOR",
"FBM_INBOUND_NOT_PROCESSABLE_OPERATOR",
"FBM_REPOSITION_PALLET_TRUCK_OPERATOR",
"FBM_INBOUND_RECEIVING_DOCAS_OPERATOR",
"FBM_OUTBOUND_PUTWALL_OPERATOR",
"FBM_OUTBOUND_PICKING_EXPERT_OPERATOR",
"FBM_RC_PICK_TO_MOVABLE_OPERATOR_EXPERT",
"FBM_MWH_INBOUND_RECEIVING_DOCAS_OPERATOR",
"FBM_QUALITY_CUBING_EXPERT",
"FBM_INBOUND_ANALYST",
"FBM_INBOUND_MASSIVE_COUNT_OPERATOR",
"FBM_REPOSITION_MOVABLE_OPERATOR",
"FBM_MWH_INBOUND_PROBLEM_SOLVER",
"FBM_MWH_OUTBOUND_DISPATCH_OPERATOR",
"FBM_MWH_DECANTING_OPERATOR",
"FBM_INBOUND_RECEIVING_OPERATOR",
"FBM_MWH_INBOUND_TEAM_LEADER",
"FBM_INBOUND_PUT_AWAY_OPERATOR_EXPERT",
"TRANSPORTATION_XD_RETURNS_OPERATOR",
"FBM_QUALITY_PS_INBOUND",
"FBM_OUTBOUND_TEAM_LEADER",
"FBM_OUTBOUND_ANALYST",
"FBM_INBOUND_TEAM_LEADER",
"PROCESS_IMPROVEMENT_TEAM_LEADER",
"FOS_DISPOSAL_OPERATOR",
"FBM_WITHDRAWAL_DISPATCH_OPERATOR",
"FBM_WITHDRAWAL_PACKING_OPERATOR",
"FBM_REMOVAL_SUPERVISOR",
"FBM_RL_TRIAGE_PUT_AWAY_OPERATOR",
"FBM_QUALITY_OPERATOR",
"FBM_MWH_OUTBOUND_TEAM_LEADER",
"FBM_OPEX_CI_LEADER",
"PLANNING_ANALYST",
"FBM_RL_RECEIVING_OPERATOR",
"FBM_MWH_OUTBOUND_SUPERVISOR",
"FBM_DISPOSAL_PICKING_OPERATOR",
"FBM_WITHDRAWAL_BATCH_SORTER_OPERATOR",
"FBM_REPOSITION_FORKLIFT_OPERATOR",
"FBM_INBOUND_DIRECT_CHECK_IN_OPERATOR",
"PROCESS_IMPROVEMENT_MANAGER",
"FBM_OUTBOUND_SUPERVISOR",
"FBM_REPOSITION_SUPERVISOR",
"FBM_QUALITY_ANALYST",
"spd_shipping_label_operator",
"FBM_LAYOUT_INBOUND_ZONES_ANALYST",
"REPRINT_LABELS",
"PROCESS_IMPROVEMENT_SUPERVISOR",
"FBM_REMOVAL_PROBLEM_SOLVER",
"FBM_RC_PROBLEM_SOLVER",
"FBM_RC_LOGISTICS_OUT_OPERATOR",
"FBM_RL_TEAM_LEADER",
"FBM_INVENTORY_REPOSITION_OPERATOR_CLAMP",
"FBM_SOP_PLANNER",
"operation_management",
"FBM_TRAINING_LEADER",
"FBM_LAYOUT_OWNER",
"FBM_INVENTORY_OPERATOR_EXPERT",
"TRANSFER",
"FBM_INBOUND_PROBLEM_SOLVER",
"SHIPPING_RETURNS_TRIAGE_ANALYST",
"TRANSPORTATION_XD_PROBLEM_SOLVER",
"FBM_CX_N2",
"FBM_OPEX_ROLE_OWNER",
"FOS_STAGING_OUT_OPERATOR",
"SHPBO_BUSINESS",
"FBM_RL_ANALYST",
"FBM_QUALITY_SUPERVISOR",
"FBM_OUTBOUND_BATCH_SORTER_OPERATOR",
"TRANSPORTATION_MM_FIELD_ANALYST_MLB",
"FBM_TRAINING_ANALYST",
"FBM_INVENTORY_ANALYST",
"FBM_RL_PROBLEM_SOLVER",
"FBM_OPEX_REGIONAL_ANALYST",
"TEMP_S&OP_PLANNER",
"N3_ASSISTANT",
"FBM_DISPOSAL_TEAM_LEADER",
"FBM_MWH_INBOUND_SUPERVISOR",
"FBM_FLOW_ANALYST",
"FBM_RC_LOGISTICS_IN_OPERATOR",
"gate_analyst",
"DRIVER_PURPOSE_ASSIGNMENT",
"FBM_DISPOSAL_DISPATCH_OPERATOR",
"FBM_INVENTORY_SUPERVISOR",
"FBM_INBOUND_PUT_AWAY_SORTER_OPERATOR",
"FBM_MWH_OUTBOUND_PICKING_FORKLIFT_OPERATOR",
"audit_movable_operator",
"SHPBO_INVOICES",
"TRACKING_PRODUCTIVITY_REP",
"TRANSPORTATION_XD_OPERATOR",
"TRANSPORTATION_SVC_OPERATOR",
"FBM_DISPOSAL_PACKING_OPERATOR",
"FOS_OPERATOR_DIVERGENCES",
"FBM_OUTBOUND_PICKING_FORKLIFT_OPERATOR",
"FBM_QUALITY_OPERATOR_EXPERT",
"TRANSPORTATION_XD_XRAY_OPERATOR",
"SHPBO_READ_ONLY",
"FBM_RL_SUPERVISOR",
"FBM_RL_CYCLE_COUNT_OPERATOR_EXPERT",
"SHPBO_LIMITED_ACCESS",
"receiving_operator",
"FOS_FACILITY_ADMIN",
"FBM_RC_PRODUCTION_SUPERVISOR",
"FBM_WITHDRAWAL_TEAM_LEADER",
"PROCESS_IMPROVEMENT_ANALYST",
"FBM_RL_FAST_CHECK_IN_OPERATOR",
"rollout_putaway_sorter",
"FBM_MWH_INBOUND_RECEIVING_OPERATOR",
"FOS_ANALYST",
"FBM_RC_SHIPPING_TEAM_LEADER",
"GATE_SECURITY",
"SHPLAN_CAPEX_ANALYST",
"LABELING",
"TRANSPORTATION_XD_RETURNS_TEAM_LEADER",
"TRANSPORTATION_XD_TEAM_LEADER",
"FOS_STAGING_ZONES",
"FBM_RL_CYCLE_COUNT_ANALYST",
"FBM_RC_LOGISTICS_SUPERVISOR",
"MATERIALS_ANALYST_FULL",
"FBM_QUALITY_TEAM_LEADER",
"FBM_LP_ANALYST",
"FBM_RC_RECEIVING_TEAM_LEADER",
"gate_viewer",
"FBM_INVENTORY_TEAM_LEADER",
"SHPBO_INVOICES_VIEW",
"FOS_OPERATOR_DEVOLUTIONS",
"DOCK_CONFIGURATOR",
"wms_it_dev",
"PRODUCT_MANAGER",
"cycle_count_auditor",
"TRACKING_PRODUCTIVITY_XD_ARBA_SUP",
"fbm_outbound_planning_read",
"withdrawal_sorter_operator",
"TRANSPORTATION_XD_SUPERVISOR",
"START_UP_SUPERVISOR",
"AP_ALF_CAPEX_APPROVER",
"ONETASK_ADMIN",
"FBM_RC_PRODUCTION_TEAM_LEADER",
"FBM_INVENTORY_ICQA_CENTRAL_ANALYST",
"canalizations_association_manager",
"wms_it_leader",
"TRACKING_PRODUCTIVITY_XD_ARBA_TL",
"PRODUCT_DATA_OPERATOR",
"FBM_LAYOUT_PUTAWAY_ZONE_LEADER",
"WMS_PI_CPG_SUPERVISOR",
"SHPBO_UCS_DEVICE",
"FOS_STAGING_OUT_ADMIN",
"TRACKING_PRODUCTIVITY_SUP",
"FOS_SUPERVISOR",
"TRANSPORTATION_XD_ANALYST",
"FBM_INVENTORY_LEADER",
"SHPBO_SHIPPING_COST",
"SHPLAN_CAPEX_AUDITOR",
"admin_pi_operation",
"FOS_OPERATOR",
"SHPBO_CX_ACCESS",
"SHPBO_UCS_SORTER_DASHBOARD",
"TRANSPORTATION_SVC_SUPERVISOR",
"TRACKING_PRODUCTIVITY_TL",
"FBM_INBOUND_LEADER",
"FOS_ADMIN",
"1P_SCARLET_USER",
"ALFRED_APPROVER",
"SHIPPING_RESTRICTIONS_VIEWER",
"PROCESS_IMPROVEMENT_COORDINATOR",
"TRANSPORTATION_SVC_ANALYST",
"IT_GROOT_DEV",
"OPERATION_ANALYST",
"SHIPPING_RETURNS_WORKFLOW_REVIEWER",
"SHPBO_SHIPPING",
"MOVABLES_SUPERVISOR",
"FBM_CX_ANALYST",
"SHPLAN_CAPEX_CONTROLLER",
"inbound_not_processable",
"CXP_APP",
"OPERATION_MANAGER",
"CUBING",
"TRANSPORTATION_SVC_RETURNS_OPERATOR",
    ]
}

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

HCsp06 = "1gP0vFS3GfSgVBiQncFECMxgWjENhVQN6TPUmPs_w78U"
pagina_HC_sp06 = "BASE"

def obter_credenciais():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    

    return creds
def logar_HC(user_name):
    creds = obter_credenciais()
    service = build("sheets", "v4", credentials=creds)
    sheet = build('sheets', 'v4', credentials=creds)

    result = service.spreadsheets().values().get(spreadsheetId=HCsp06,
                                                         range=pagina_HC_sp06).execute()
    
    values = result.get('values', [])
    
    for i, row in enumerate(values):
        if row and row[7] == user_name:
            # Encontrou o usuário, retorna os valores das colunas N e S
            coluna_n = row[13] if len(row) > 13 else None
            coluna_s = row[18] if len(row) > 18 else None
            return coluna_n, coluna_s

    # Usuário não encontrado
    return None, None

def buscar_informacoes(user_name):
    coluna_n, coluna_s = logar_HC(user_name)
    return coluna_n, coluna_s


def determinar_bolhas_disponiveis(coluna_n, coluna_s):
    if coluna_n in ["REP DE ENVIO 1", "REP DE ENVIO 2", "REP DE ENVIO 3"] and coluna_s == "outbound":
        return ["bolha1", "bolha2", "bolha3"]
    elif coluna_n in ["OPERADOR LOGÍSTICO 1", "OPERADOR LOGÍSTICO 2"] and coluna_s == "outbound":
        return ["bolha3", "bolha4", "bolha6"]
    elif coluna_n in ["REP DE ENVIO 1", "REP DE ENVIO 2", "REP DE ENVIO 3"] and coluna_s == "INBOUND":
        return ["bolha7", "bolha8", "bolha9"]
    elif coluna_n in ["OPERADOR LOGÍSTICO 1", "OPERADOR LOGÍSTICO 2"] and coluna_s == "INBOUND":
        return ["bolha10", "bolha11", "bolha12"]
    elif coluna_n in ["OPERADOR LOGÍSTICO 1", "OPERADOR LOGÍSTICO 2"] and coluna_s == "STAFF":
        return ["bolha13", "bolha14", "bolha15"]
    else:
        return []


def buscar():
    user_name = st.text_input("Insira o usuário")
    if st.button("Buscar Informações"):
        if user_name:
            coluna_n, coluna_s = buscar_informacoes(user_name)
            
            if coluna_n is not None and coluna_s is not None:
                st.success(f"Informações encontradas para {user_name}: Coluna N: {coluna_n}, Coluna S: {coluna_s}")




                if tipo_alteracao == "gestao":
                    alterar_gestao(coluna_n, coluna_s)
                
                elif tipo_alteracao == "bolha":
                    alterar_bolha(coluna_n, coluna_s)
                
                elif tipo_alteracao == "processo madre":
                    alterar_processo_madre()

            else:
                st.warning(f"Usuário {user_name} não encontrado na planilha.")
        else:
            st.warning("Por favor, insira o nome do usuário para buscar.")

def alterar_gestao(coluna_n, coluna_s):
    nome_gestor = st.text_input("Nome do gestor:", key="gestor_input")
    st.success(f"Alteração de gestão para {nome_gestor} realizada com sucesso.")

def alterar_bolha(coluna_n, coluna_s):
    bolhas_disponiveis = determinar_bolhas_disponiveis(coluna_n, coluna_s)
    if bolhas_disponiveis:
        escolha_bolha = st.selectbox("Escolha a bolha:", bolhas_disponiveis, key="bolha_input")
        st.success(f"Bolha {escolha_bolha} adicionada com sucesso.")
    else:
        st.warning("Não há bolhas disponíveis para seleção.")

def alterar_processo_madre():
    processo_madre = st.text_input("Qual processo?", key="processo_input")
    st.success(f"Alteração de processo madre para {processo_madre} realizada com sucesso.")




if __name__ == "__main__":
    tipo_alteracao = st.radio("Qual tipo de alteração?", ["gestao", "bolha", "processo madre"])
    buscar()
